import asyncio
import aiohttp
from selectolax.parser import HTMLParser
import urllib.parse
import time
import sys

# CONFIGURATION
BASE_URL = "https://ikarvon.uz"
MAX_PAGES = 5
DETAIL_SEM = 15          # Max parallel detail page requests
# DETAIL_TIMEOUT = 8       # Seconds per detail page
# SEARCH_TIMEOUT = 5       # Seconds per search API call
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    "Accept": "text/html,application/json",
    "Connection": "keep-alive",
}


def parse_details(html, product_name_hint=""):
    """Parse product detail HTML and return extracted fields (CPU-bound, no I/O)"""
    tree = HTMLParser(html)
    details = {
        "brand": None,
        "product_category": None,
        "stock_status": "Нет в наличии",
        "stock_quantity": 0,
        "seller": None,
        "seller_ranking": None,
        "price_unit": "шт",
    }

    # Brand
    for strong in tree.css('ul.product-characters__list strong'):
        text = strong.text(strip=True)
        if text and len(text) > 1:
            details["brand"] = text
            break

    # Category (second-to-last breadcrumb)
    breadcrumbs = tree.css('ol.breadcrumb li.breadcrumb-item a')
    if len(breadcrumbs) >= 2:
        details["product_category"] = breadcrumbs[-2].text(strip=True)

    # Stock status — preserve original Russian text
    stock_elem = tree.css_first('span.product-head__status')
    if stock_elem:
        stock_text = stock_elem.text(strip=True)
        details["stock_status"] = stock_text
        if "нет в наличии" in stock_text.lower():
            details["stock_quantity"] = 0
        elif "наличии" in stock_text.lower():
            details["stock_quantity"] = 10

    # Seller (JS-rendered, rarely available in static HTML)
    partner = tree.css_first('div[data-partner-code]')
    if partner:
        code = partner.attributes.get('data-partner-code', '').strip()
        if code:
            details["seller"] = code

    # Seller rating
    stars = tree.css('ul.star-list li')
    if stars:
        details["seller_ranking"] = len(stars)

    # Price unit: check the price label on page for "/кг", "/л", "/м" indicators
    price_label = tree.css_first('.product-head__price, .product-price')
    if price_label:
        pt = price_label.text(strip=True).lower()
        if "/кг" in pt or "за кг" in pt:
            details["price_unit"] = "кг"
        elif "/л" in pt or "за л" in pt:
            details["price_unit"] = "л"
        elif "/м" in pt or "за м" in pt:
            details["price_unit"] = "м"

    return details


async def fetch_detail(session, url, sem):
    """Fetch one product detail page with semaphore rate-limiting."""
    async with sem:
        try:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=DETAIL_TIMEOUT)) as resp:
                if resp.status != 200:
                    return url, None
                html = await resp.text(encoding='utf-8', errors='replace')
                return url, html
        except Exception:
            return url, None


def format_product(product, details=None):
    """Format product data from JSON API + scraped details"""
    if details is None:
        details = {}
    return {
        "id": product.get("id"),
        "name": product.get("name", "N/A"),
        "price": product.get("current_price_formatted", "N/A"),
        "price_raw": product.get("current_price", 0),
        "currency": "UZS",
        "price_unit": details.get("price_unit", "шт"),
        "url": product.get("url", ""),
        "img": f"{BASE_URL}{product.get('small_img', '')}",
        "img_full": f"{BASE_URL}{product.get('img', '')}",
        "brand": details.get("brand"),
        "product_category": details.get("product_category"),
        "stock_status": details.get("stock_status", "Нет в наличии"),
        "stock_quantity": details.get("stock_quantity", 0),
        "seller": details.get("seller"),
        "seller_ranking": details.get("seller_ranking"),
    }


async def search(session, query, page=1):
    """Hit the JSON search API and return the products list"""
    encoded = urllib.parse.quote(query)
    url = f"{BASE_URL}/search?q={encoded}&json=1&page={page}"
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=SEARCH_TIMEOUT)) as resp:
            if resp.status != 200:
                return []
            data = await resp.json(content_type=None)
        return data.get("products", [])
    except Exception:
        return []


async def main():
    sys.stdout.reconfigure(encoding='utf-8')

    query = input("What are you searching?: ").strip()
    if not query:
        print("Empty query!")
        return

    start = time.time()

    connector = aiohttp.TCPConnector(limit=50, limit_per_host=30, keepalive_timeout=15)
    async with aiohttp.ClientSession(headers=HEADERS, connector=connector) as session:

        # Phase 1: Search API — all pages in parallel
        print(f"\nSearching for '{query}'...")
        page_results = await asyncio.gather(
            *[search(session, query, p) for p in range(1, MAX_PAGES + 1)]
        )

        # Flatten + deduplicate by product ID
        seen_ids = set()
        all_products = []
        for products in page_results:
            for p in products:
                pid = p.get("id")
                if pid and pid not in seen_ids:
                    seen_ids.add(pid)
                    all_products.append(p)

        if not all_products:
            print("No results found!")
            return

        t1 = time.time()
        print(f"Found {len(all_products)} unique products ({round(t1 - start, 1)}s)")

        # Phase 2: Scrape only UNIQUE detail URLs in parallel
        unique_urls = list({p.get("url", "") for p in all_products if p.get("url")})
        sem = asyncio.Semaphore(DETAIL_SEM)
        fetch_tasks = [fetch_detail(session, url, sem) for url in unique_urls]
        fetch_results = await asyncio.gather(*fetch_tasks)

        # Build URL → HTML cache
        html_cache = {url: html for url, html in fetch_results if html}

        t2 = time.time()
        print(f"Scraped {len(html_cache)}/{len(unique_urls)} detail pages ({round(t2 - t1, 1)}s)")

        # Phase 3: Parse HTML (CPU-only, fast) and map back to products
        url_details = {}
        for url, html in html_cache.items():
            url_details[url] = parse_details(html)

        # Build final results
        results = []
        for p in all_products:
            url = p.get("url", "")
            details = url_details.get(url)
            results.append(format_product(p, details))

        # Print results
        print(f"\n{'='*80}")
        print(f"Finished: {len(results)} products")
        print(f"{'='*80}\n")

        for i, p in enumerate(results, 1):
            print(f"{i}. {p['name']}")
            print(f"     Price:          {p['price']} {p['currency']} / {p['price_unit']}")
            print(f"     Brand:          {p['brand'] or 'N/A'}")
            print(f"     Category:       {p['product_category'] or 'N/A'}")
            print(f"     Stock:          {p['stock_status']} ({p['stock_quantity']} units)")
            print(f"     Seller:         {p['seller'] or 'N/A'}")
            print(f"     Seller Rating:  {'⭐' * (p['seller_ranking'] or 0) if p['seller_ranking'] else 'N/A'} ({p['seller_ranking'] or 0}/5)")
            print(f"     Img URL:        {p['img']}")
            print(f"     Link:           {p['url']}")
            print(f"   {'-'*76}")

    elapsed = time.time() - start
    print(f"\n{'='*80}")
    print(f"Done in {round(elapsed, 2)} seconds  |  {round(len(results)/elapsed, 1)} products/sec")
    print(f"{'='*80}")


if __name__ == "__main__":
    asyncio.run(main())
