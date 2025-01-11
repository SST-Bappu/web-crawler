import asyncio

from web_crawler.crawler.crawler import WebCrawler

if __name__ == "__main__":
    start_urls = ["https://www.amazon.in", "https://www.flipkart.com"]
    crawler = WebCrawler(start_urls, max_depth=2)
    
    
    async def main():
        await crawler.crawl()
        crawler.save_results()
        print("Crawl finished. Results saved.")
    
    
    asyncio.run(main())