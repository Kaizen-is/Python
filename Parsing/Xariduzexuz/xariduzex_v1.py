from playwright.sync_api import sync_playwright
import time


def scrape_xarid_uzex():
    query = input("Nima qidiramiz?: ")

    with sync_playwright() as p:
        # slow_mo helps the site process the search before we grab data
        browser = p.chromium.launch(headless=False, slow_mo=200)
        context = browser.new_context(viewport={"width": 1920, "height": 1080})
        page = context.new_page()

        try:
            print("[*] Sahifa yuklanmoqda...")
            page.goto("https://xarid.uzex.uz/shop/products-list/eshop", wait_until="networkidle")

            # 1. Filter Panel Logic
            print("[*] Filtr ochilmoqda...")
            page.click("button.filter-toggle-down-btn")
            time.sleep(2)

            # 2. Search Input (ID from previous screenshot)
            page.fill("input#keyword", query)
            print(f"[*] '{query}' qidirilmoqda...")

            # Click the Search button (btn-primary btn-lg)
            page.click("button.btn-primary.btn-lg:has-text('Qidirish')")

            # 3. Wait for Results to Populate
            print("[*] Natijalar yuklanishini kutmoqdaman (10 soniya)...")
            # Wait for any of your provided classes to appear
            page.wait_for_selector(".product__title", timeout=15000)
            time.sleep(5)

            # 4. DIRECT JAVASCRIPT EXTRACTION (The "Senior" Way)
            # We use the exact classes you provided to map the data
            results = page.evaluate("""
                () => {
                    const data = [];
                    // We find all title elements as the primary anchor
                    const titles = document.querySelectorAll('.product__title');

                    titles.forEach(titleEl => {
                        // Find the container that holds this product (usually a .card or .item)
                        const container = titleEl.closest('.product-item-wrapper') || titleEl.parentElement.parentElement;

                        if (container) {
                            const name = titleEl.innerText.trim();
                            const priceEl = container.querySelector('.product__price');
                            const amountEl = container.querySelector('.float-right.smaller-size-custom-style');
                            const marketEl = container.querySelector('.smaller-size-custom-style');
                            const linkEl = container.querySelector('a');

                            data.push({
                                name: name,
                                price: priceEl ? priceEl.innerText.trim() : 'N/A',
                                amount: amountEl ? amountEl.innerText.trim() : 'N/A',
                                market: marketEl ? marketEl.innerText.trim() : 'N/A',
                                link: linkEl ? linkEl.href : ''
                            });
                        }
                    });
                    return data;
                }
            """)

            # 5. Output Results
            if not results:
                print("[-] Hech narsa topilmadi. Selektorlar mos kelmadi.")
                return

            print(f"\n[+] {len(results)} ta mahsulot topildi:\n")
            for i, item in enumerate(results, 1):
                print(f"{i}. {item['name']}")
                print(f"   Narxi: {item['price']}")
                print(f"   Miqdori: {item['amount']}")
                print(f"   Sotuvchi/Market: {item['market']}")
                print(f"   Link: {item['link']}\n")

        except Exception as e:
            print(f"[!] Xatolik yuz berdi: {e}")
        finally:
            print("[*] Jarayon yakunlandi.")
            time.sleep(10)
            browser.close()


if __name__ == "__main__":
    scrape_xarid_uzex()