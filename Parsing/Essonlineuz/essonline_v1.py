import asyncio
import aiohttp
from selectolax.parser import HTMLParser
import urllib.parse
import time
import sys
import re

# CONFIGURATION
BASE_URL = "https://essonline.uz"
MAX_PAGES = 3
PRODUCTS_PER_PAGE = 18
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "text/html",
    "Accept-Language": "ru-RU,ru;q=0.9,en;q=0.8",
    "Connection": "keep-alive",
}

def extract_brand_from_name(product_name):
    """Extract brand from uppercase words in product name"""
    words = product_name.split()
    brand_words = []
    for word in words:
        if word.isupper() and len(word) > 1:
            brand_words.append(word)
        elif any(c.isupper() for c in word) and not word.endswith(('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')):
            brand_words.append(word)
    return " ".join(brand_words) if brand_words else None

def extract_products_from_category(html, category_url):
    """Extract products directly from category page HTML"""
    tree = HTMLParser(html)
    
    # Get category name from page title
    category = None
    title = tree.css_first('title')
    if title:
        title_text = title.text(strip=True)
        category = title_text.split(' в Ташкенте')[0]
    
    # Find product container
    container = tree.css_first('.product-page--items')
    if not container:
        return []
    
    products = []
    
    # Find all price containers (each represents a product)
    price_containers = container.css('.product-page__item--prscrt')
    
    for price_container in price_containers:
        product_container = price_container.parent
        if not product_container:
            continue
        
        # Extract product info
        product = {
            "name": None,
            "brand": None,
            "price": None,
            "currency": "UZS",
            "price_unit": "шт",
            "category": category,
            "stock_status": None,
            "stock_quantity": None,
            "seller_name": None,
            "seller_ranking": None,
            "img_url": None,
            "product_url": category_url,
        }
        
        # Get all text from container
        container_text = product_container.text(strip=True)
        
        # Extract product name - handle compressed text format
        # Remove "В наличии" and extract name between code and specs
        clean_text = container_text.replace('В наличии', ' ')
        
        # Look for pattern: Код:[number] [product name] [specs]
        import re
        code_match = re.search(r'Код:(\d+)', clean_text)
        if code_match:
            # Extract text after the code
            after_code = clean_text[code_match.end():].strip()
            
            # Product name is the first part before any spec indicators
            spec_indicators = ['Тип устройства:', 'Количество полюсов:', 'Напряжение', 'Номинальное', 'Частота', 'Категория применения:', 'Электрическая износостойкость:', 'сум', 'В КОРЗИНУ']
            
            for indicator in spec_indicators:
                if indicator in after_code:
                    product_name = after_code.split(indicator)[0].strip()
                    if len(product_name) > 5:
                        product["name"] = product_name
                        product["brand"] = extract_brand_from_name(product_name)
                        break
            else:
                # If no spec indicators found, take everything up to first number+letter pattern
                parts = re.split(r'(\d+[A-ZА-Я])', after_code)
                if len(parts) > 1:
                    product_name = parts[0].strip()
                    if len(product_name) > 5:
                        product["name"] = product_name
                        product["brand"] = extract_brand_from_name(product_name)
        
        # Extract price
        price_elem = price_container.css_first('[class*="price"]')
        if price_elem:
            price_text = price_elem.text(strip=True)
            price_match = re.search(r'([\d\s]+)', price_text)
            if price_match:
                price_str = price_match.group(1).replace(' ', '')
                try:
                    product["price"] = int(price_str)
                except ValueError:
                    pass
        
        # Stock status
        if 'в наличии' in container_text.lower():
            product["stock_status"] = "В наличии"
            product["stock_quantity"] = 10
        else:
            product["stock_status"] = "Нет в наличии"
            product["stock_quantity"] = 0
        
        # Image - look in parent container (.product-page__item) where images are located
        parent_container = product_container.parent
        if parent_container:
            img = parent_container.css_first('img')
            if img:
                src = img.attributes.get('src', '')
                if src:
                    if src.startswith('http'):
                        product["img_url"] = src
                    else:
                        product["img_url"] = f"{BASE_URL}{src}"
        
        if product["name"]:  # Only add if we found a name
            products.append(product)
    
    return products

async def search_categories(session, query, page=1):
    """Search for product categories on essonline.uz"""
    encoded = urllib.parse.quote(query)
    
    # Use the search endpoint
    search_url = f"{BASE_URL}/search?q={encoded}"
    if page > 1:
        search_url += f"&page={page}"
    
    try:
        async with session.get(search_url, timeout=aiohttp.ClientTimeout(total=8)) as resp:
            if resp.status != 200:
                print(f"  HTTP {resp.status} for {search_url}")
                return []
            
            html = await resp.text(encoding='utf-8', errors='replace')
            tree = HTMLParser(html)
            
            # Look for category links in search results
            category_links = []
            
            # Essonline shows category links, not individual products
            links = tree.css('a[href*="/"]')
            for link in links:
                href = link.attributes.get('href', '')
                text = link.text(strip=True)
                
                # Skip navigation and look for meaningful category links
                if (href and not href.startswith('#') and 
                    not href.startswith('tel:') and
                    not any(skip in href for skip in ['/login', '/register', '/cart', '/wishlist', '/site', '/search']) and
                    len(text) > 10 and  # Meaningful text
                    not any(nav in text.lower() for nav in ['вход', 'регистрация', 'корзина', 'избранные', 'новые товары', 'о компании', '+998'])):  # Skip navigation
                    
                    if href.startswith('http'):
                        full_url = href
                    else:
                        full_url = f"{BASE_URL}{href}"
                    
                    category_links.append({
                        "url": full_url,
                        "name": text
                    })
            
            return category_links[:PRODUCTS_PER_PAGE]
            
    except Exception as e:
        print(f"  Error searching: {e}")
        return []

async def fetch_category_products(session, category_url, sem):
    """Fetch products from a category page"""
    async with sem:
        try:
            async with session.get(category_url, timeout=aiohttp.ClientTimeout(total=8)) as resp:
                if resp.status != 200:
                    return category_url, []
                html = await resp.text(encoding='utf-8', errors='replace')
                products = extract_products_from_category(html, category_url)
                return category_url, products
        except Exception:
            return category_url, []

async def main():
    sys.stdout.reconfigure(encoding='utf-8')
    
    query = input("What are you searching for on essonline.uz?: ").strip()
    if not query:
        print("Empty query!")
        return
    
    start = time.time()
    
    connector = aiohttp.TCPConnector(limit=50, limit_per_host=30, keepalive_timeout=15)
    async with aiohttp.ClientSession(headers=HEADERS, connector=connector) as session:
        
        print(f"\nSearching for '{query}' on essonline.uz...")
        
        # Search for categories (not individual products)
        search_tasks = [search_categories(session, query, page) for page in range(1, MAX_PAGES + 1)]
        page_results = await asyncio.gather(*search_tasks)
        
        # Flatten and deduplicate categories
        all_categories = []
        seen_urls = set()
        for page_categories in page_results:
            for category in page_categories:
                url = category.get('url', '')
                if url and url not in seen_urls:
                    seen_urls.add(url)
                    all_categories.append(category)
        
        if not all_categories:
            print("No categories found!")
            return
        
        print(f"Found {len(all_categories)} categories")
        
        # Fetch products from categories in parallel
        sem = asyncio.Semaphore(10)  # Limit concurrent category requests
        category_tasks = [fetch_category_products(session, cat.get('url', ''), sem) for cat in all_categories]
        category_results = await asyncio.gather(*category_tasks)
        
        # Collect all products
        all_products = []
        for category_url, products in category_results:
            all_products.extend(products)
        
        print(f"Extracted {len(all_products)} products from categories")
        
        # Print results
        print(f"\n{'='*80}")
        print(f"Finished: {len(all_products)} products")
        print(f"{'='*80}\n")
        
        for i, p in enumerate(all_products, 1):
            print(f"{i}. {p.get('name', 'N/A')}")
            print(f"     Brand:          {p['brand'] or 'N/A'}")
            print(f"     Category:       {p['category'] or 'N/A'}")
            print(f"     Price:          {p['price'] or 'N/A'} {p['currency'] or ''} / {p['price_unit'] or 'N/A'}")
            print(f"     Stock:          {p['stock_status'] or 'N/A'} ({p['stock_quantity'] or 0} units)")
            print(f"     Seller:         {p['seller_name'] or 'N/A'}")
            print(f"     Img URL:        {p['img_url'] or 'N/A'}")
            print(f"     Link:           {p['product_url']}")
            print(f"   {'-'*76}")
    
    elapsed = time.time() - start
    print(f"\n{'='*80}")
    print(f"Done in {round(elapsed, 2)} seconds")
    print(f"{'='*80}")

if __name__ == "__main__":
    asyncio.run(main())