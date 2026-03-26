import asyncio
import time
from playwright.async_api import async_playwright
import urllib.parse

BASE_URL = "https://openmarket.uz"


async def fetch_product_data(context, link, semaphore):
    """Fetch individual product details"""
    async with semaphore:
        page = await context.new_page()

        try:
            await page.goto(link, wait_until="domcontentloaded", timeout=15000)
            
            # Wait for key elements
            await asyncio.gather(
                page.wait_for_selector("h1", timeout=10000),
                return_exceptions=True
            )
            
            # Extract ALL data in ONE JavaScript call
            product_data = await page.evaluate("""
                () => {
                    const data = {};
                    
                    // Name
                    const nameEl = document.querySelector('h1');
                    data.name = nameEl ? nameEl.innerText.trim() : '';
                    
                    // Price
                    const priceEl = document.querySelector('div.flex.flex-wrap.items-end.gap-1');
                    data.price = priceEl ? priceEl.innerText.replace(/\\n/g, ' ').trim() : 'N/A';
                    
                    // Description
                    const descEl = document.querySelector('.bodyText-sm-regular.text-textBody');
                    data.description = descEl ? descEl.innerText.replace(/\\n/g, ' ').trim() : 'No description';
                    
                    // Seller
                    const sellerEl = document.querySelector('.text-textBody.line-clamp-1');
                    data.seller = sellerEl ? sellerEl.innerText.trim() : 'Unknown';
                    
                    return data;
                }
            """)

            name = product_data.get('name', '')
            
            # Return ALL products (no score filtering)
            if name:
                return {
                    "name": name,
                    "price": product_data.get('price', 'N/A'),
                    "seller": product_data.get('seller', 'Unknown'),
                    "description": product_data.get('description', 'No description')[:200],
                    "link": link
                }
            else:
                return None

        except Exception as e:
            return None

        finally:
            await page.close()


async def scrape_search_page(page, page_number=1):
    """Scrape product links from current search results page"""
    try:
        print(f"[*] Scraping page {page_number}...")

        # Wait for products to load
        await page.wait_for_selector("a[href*='/products/']", timeout=10000)
        await asyncio.sleep(1)
        
        # Extract all product links using JavaScript
        links = await page.evaluate(f"""
            () => {{
                const baseUrl = '{BASE_URL}';
                const elements = document.querySelectorAll("a[href*='/products/']");
                const links = new Set();
                
                elements.forEach(el => {{
                    let href = el.getAttribute('href');
                    if (href) {{
                        // Make absolute URL
                        if (href.startsWith('/')) {{
                            href = baseUrl + href;
                        }}
                        links.add(href);
                    }}
                }});
                
                return Array.from(links);
            }}
        """)
        
        print(f"  → Found {len(links)} products on page {page_number}")
        return links
        
    except Exception as e:
        print(f"Error on page {page_number}: {e}")
        return []



async def navigate_to_next_page(page, page_number):
    """Navigate to next page using pagination button"""
    try:
        # The pagination button is an <a> tag with aria-label="Go to next page"
        # It has href="/ru/search/{query}?page=2"
        
        # Method 1: Try clicking the link directly
        next_link = await page.query_selector('a[aria-label="Go to next page"]')
        
        if next_link:
            # Check if link exists and has href
            href = await next_link.get_attribute('href')
            if href:
                print(f"[*] Navigating to page {page_number + 1}...")
                await next_link.click()
                await asyncio.sleep(2)  # Wait for page transition
                return True

    except Exception as e:
        print(f"Pagination error: {e}")
        return False


async def main():
    query = input("What are you searching?: ").strip()
    max_pages = int(input("How many pages to scrape? (1-10, default 3): ") or "3")
    max_pages = min(max_pages, 10)
    
    start_time = time.time()

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage',
                '--disable-gpu',
                '--no-sandbox'
            ]
        )
        
        context = await browser.new_context(
            locale="ru-RU",
            viewport={"width": 1920, "height": 1080},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )

        # Block images/CSS for speed
        await context.route("**/*.{png,jpg,jpeg,gif,svg,css,woff,woff2}", lambda route: route.abort())

        page = await context.new_page()
        
        # FIXED: Use direct search URL instead of form submission
        print(f"[*] Searching for '{query}'...")
        
        # URL encode the query
        encoded_query = urllib.parse.quote(query)
        search_url = f"{BASE_URL}/ru/search/{encoded_query}"
        
        print(f"[*] Opening search URL: {search_url}")
        await page.goto(search_url, wait_until="domcontentloaded", timeout=20000)
        
        # Wait for search results to load
        await asyncio.sleep(2)



        # ASYNC PARALLEL PAGE SCRAPING
        # Instead of scraping pages one by one, open multiple pages simultaneously
        
        print(f"[*] Opening {max_pages} search pages simultaneously...\n")
        
        # Create multiple browser pages at once
        pages = []
        for i in range(max_pages):
            new_page = await context.new_page()
            pages.append(new_page)
        
        # Build URLs for all pages
        encoded_query = urllib.parse.quote(query)
        page_urls = []
        for page_num in range(1, max_pages + 1):
            if page_num == 1:
                url = f"{BASE_URL}/ru/search/{encoded_query}"
            else:
                url = f"{BASE_URL}/ru/search/{encoded_query}?page={page_num}"
            page_urls.append((page_num, url))
        
        # Navigate to all pages in parallel
        async def navigate_and_scrape(page_obj, page_num, url):
            try:
                print(f"[*] Loading page {page_num}...")
                await page_obj.goto(url, wait_until="domcontentloaded", timeout=15000)
                await asyncio.sleep(1)
                
                # Scrape this page
                links = await scrape_search_page(page_obj, page_num)
                return links
            except Exception as e:
                print(f"Error loading page {page_num}: {e}")
                return []
        
        # Execute all page scraping in parallel
        tasks = [
            navigate_and_scrape(pages[i], page_urls[i][0], page_urls[i][1])
            for i in range(len(pages))
        ]
        
        results_per_page = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Collect all links
        all_links = []
        for links in results_per_page:
            if isinstance(links, list):
                all_links.extend(links)
        
        # Close all search pages
        for p in pages:
            await p.close()
        
        # Remove duplicates
        all_links = list(set(all_links))
        await page.close()

        if not all_links:
            print("[-] No products found.")
            await browser.close()
            return

        print(f"\n[+] Total {len(all_links)} unique products found across {max_pages} page(s)")
        print(f"[*] Fetching product details (async)...\n")

        # Increase concurrency for speed
        semaphore = asyncio.Semaphore(10)

        tasks = [
            fetch_product_data(context, link, semaphore)
            for link in all_links
        ]

        raw_results = await asyncio.gather(*tasks, return_exceptions=True)

        # Filter out None results
        results = [r for r in raw_results if r and isinstance(r, dict)]

        await browser.close()

        # Display results
        if results:
            print(f"\n{'='*80}")
            print(f"FINAL RESULTS: {len(results)} PRODUCTS FOUND")
            print(f"{'='*80}\n")
            
            for i, r in enumerate(results, 1):
                print(f"{i}. {r['name']}")
                print(f"Price: {r['price']}")
                print(f"Seller: {r['seller']}")
                print(f"Description: {r['description']}...")
                print(f"Link: {r['link']}")
                print(f"   {'-'*76}")
        else:
            print("[-] No products found.")

        elapsed = time.time() - start_time
        print(f"\n{'='*80}")
        print(f"✓ FINISHED in {round(elapsed, 2)} seconds!")
        print(f"  Speed: {round(len(all_links) / elapsed, 2)} products/second")
        print(f"{'='*80}")


if __name__ == "__main__":
    asyncio.run(main())
