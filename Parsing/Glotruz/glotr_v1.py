import asyncio
import aiohttp
from selectolax.parser import HTMLParser
import time
import re

# KONFIGURATSIYA
BASE_URL = "https://glotr.uz"
SEARCH_TERM = input("What are you searching!: ")
MAX_CONCURRENT = 50  # Bir vaqtda maksimal so'rovlar soni
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.69 Safari/537.36",
    "Accept-Language": "uz-UZ,uz;q=0.9,en;q=0.8",
}


def parse_cards(html):
    """HTML dan mahsulot kartochkalarini parse qilish"""
    tree = HTMLParser(html)
    products = []
    cards = tree.css("div.product-card__parent")
    for card in cards:
        a = card.css_first("a.product-card__link")
        if not a: continue

        title = a.text(strip=True)
        href = a.attributes.get("href", "")
        link = BASE_URL + href if href.startswith("/") else href

        # Narxni raqamga o'tkazish
        price = None
        price_el = card.css_first("div.price-retail.proposal-price")
        if price_el:
            price_digits = re.sub(r"\D", "", price_el.text())
            if price_digits: price = int(price_digits)

        stock_el = card.css_first("span.text-stock")
        stock = stock_el.text(strip=True) if stock_el else "Noma'lum"

        products.append({
            "title": title,
            "price": price,
            "link": link,
            "stock": stock,
        })
    return products, tree


MAX_PAGES = 10


async def fetch_search_page(session, page):
    """Bitta qidiruv sahifasini yuklash"""
    url = f"{BASE_URL}/search/?term={SEARCH_TERM}&page={page}"
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=30)) as response:
            if response.status != 200:
                return []
            html = await response.text()
        products, _ = parse_cards(html)
        print(f"\U0001f4c4 Sahifa {page}: {len(products)} ta mahsulot")
        return products
    except Exception as e:
        print(f"\u274c Sahifa {page} xatolik: {e}")
        return []


async def scrape_search_results(session):
    """Qidiruv natijalaridan asosiy ma'lumotlarni PARALLEL yig'ish"""
    print(f"\U0001f680 Qidiruv boshlandi: {SEARCH_TERM}")

    # 1-dan MAX_PAGES gacha sahifalarni PARALLEL yuklash
    urls = [f"{BASE_URL}/search/?term={SEARCH_TERM}&page={p}" for p in range(1, MAX_PAGES + 1)]
    for u in urls:
        print(f"  {u}")

    tasks = [
        fetch_search_page(session, page)
        for page in range(1, MAX_PAGES + 1)
    ]
    results = await asyncio.gather(*tasks)
    all_products = []
    for page_products in results:
        all_products.extend(page_products)

    print(f"\u2705 Jami {len(all_products)} ta mahsulot topildi.")

    # # Topilgan mahsulotlarni chiqarish
    # for i, p in enumerate(all_products, 1):
    #     print(f"\n--- Mahsulot #{i} ---")
    #     print(f"  Nomi:    {p['title']}")
    #     print(f"  Narxi:   {p['price']} so'm" if p['price'] else "  Narxi:   Noma'lum")
    #     print(f"  Mavjud:  {p['stock']}")
    #     print(f"  Havola:  {p['link']}")

    return all_products


async def fetch_product_detail(session, semaphore, i, product):
    """Bitta mahsulot sahifasidan ma'lumot olish"""
    link = product["link"]
    async with semaphore:
        try:
            async with session.get(link, timeout=aiohttp.ClientTimeout(total=20)) as res:
                if res.status != 200:
                    return
                html = await res.text()

            tree = HTMLParser(html)

            # Selectorlar skrinshotlaringiz asosida
            desc_el = tree.css_first("div.product-description.a-table.table-flex")
            price_el = tree.css_first("div.price-retail.proposal-price")
            seller_el = tree.css_first("div.seller-company__info-content strong.text-overflow-one-line")
            rank_el = tree.css_first("div.rating span")
            loc_el = tree.css_first("div.seller-company__info-content span.text-overflow-two-line")
            description = desc_el.text(strip=True) if desc_el else "Noma'lum"
            price_info = price_el.text(strip=True) if price_el else "Noma'lum"
            seller_name = seller_el.text(strip=True) if seller_el else "Noma'lum"
            seller_rank = rank_el.text(strip=True) if rank_el else "Noma'lum"
            seller_loc = loc_el.text(strip=True) if loc_el else "Noma'lum"

            # print(f"\n📦 Mahsulot #{i}: {product['title']}")
            # print(f"  Tavsif:          {description}")
            # print(f"  Narx (batafsil): {price_info}")
            # print(f"  Sotuvchi:        {seller_name}")
            # print(f"  Reyting:         {seller_rank}")
            # print(f"  Joylashuv:       {seller_loc}")

        except Exception as e:
            print(f"⚠️ Mahsulot #{i} da xatolik: {e}")


async def fill_product_details(session, products):
    """Barcha mahsulot sahifalariga PARALLEL kirib ma'lumotlarni to'ldirish"""
    if not products:
        print("ℹ️ Mahsulotlar topilmadi.")
        return

    print(f"\n🔍 {len(products)} ta mahsulotning ichki ma'lumotlari PARALLEL yig'ilmoqda...")

    semaphore = asyncio.Semaphore(MAX_CONCURRENT)
    tasks = [
        fetch_product_detail(session, semaphore, i, product)
        for i, product in enumerate(products, 1)
    ]
    await asyncio.gather(*tasks)

    print("\n✨ Jarayon yakunlandi!")


async def main():
    start = time.time()
    connector = aiohttp.TCPConnector(limit=100, limit_per_host=100)
    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        products = await scrape_search_results(session)
        await fill_product_details(session, products)
    print(f"⏱️ Jami sarflangan vaqt: {time.time() - start:.2f} soniya")

if __name__ == "__main__":
    asyncio.run(main())