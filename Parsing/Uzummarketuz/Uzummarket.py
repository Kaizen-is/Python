from playwright.sync_api import sync_playwright
import time  # <- bu modulni import qilamiz

SEARCH = input("What are you searching?: ")

start_time = time.time()  # Kod boshlanish vaqti



UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/122.0.6261.69 Safari/537.36"
)

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context(
        user_agent=UA,
        locale="uz-UZ",
        viewport={"width": 1366, "height": 768}
    )
    page = context.new_page()

    
    page.goto(f"https://uzum.uz/search?query={SEARCH}", timeout=60000)

    # Mahsulotlar chiqishini kutamiz
    page.wait_for_selector("a[href*='/product/']", timeout=30000)

    # Scroll (lazy load uchun)
    for _ in range(3):
        page.mouse.wheel(0, 3000)
        page.wait_for_timeout(1500)

    products = page.query_selector_all("a[href*='/product/']")

    results = []

    for p in products:
        title = p.inner_text().strip()
        link = p.get_attribute("href")

        if not title or not link:
            continue

        results.append({
            "title": title,
            "link": "https://uzum.uz" + link
        })

    browser.close()

end_time = time.time()  # Kod tugash vaqti
duration = end_time - start_time  # seconds
minutes = int(duration // 60)
seconds = int(duration % 60)

# Natijani chiqaramiz
for i, item in enumerate(results[:20], 1):
    print(f"{i}. {item['title']}")
    print(f"   {item['link']}")

print(f"\nKod run duration: {minutes} min {seconds} sec ({duration:.2f} sec)")


