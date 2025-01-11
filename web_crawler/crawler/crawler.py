import asyncio
from collections import defaultdict

import aiohttp

from web_crawler.crawler.exporter.exporter import JsonResultSaver
from web_crawler.crawler.fetcher.fetcher import AsyncHtmlFetcher
from web_crawler.crawler.filters.filter import DefaultUrlFilter
from web_crawler.crawler.parser.parser import BeautifulSoupParser
from web_crawler.logs.logger import Logger


class WebCrawler:
    def __init__(self, start_urls, max_depth=2, timeout=10):
        self.start_urls = start_urls
        self.max_depth = max_depth
        self.timeout = timeout
        self.visited_urls = defaultdict(set)
        self.base_urls = set(start_urls)
        self.results = []
        
        # initializing logger with class name
        self.logger = Logger(self.__class__.__name__).get_logger()
        
        # initializing fethcer, parser, filters and exporter instances
        self.fetcher = AsyncHtmlFetcher(self.logger)
        self.parser = BeautifulSoupParser(self.logger)
        self.filter = DefaultUrlFilter(self.logger)
        self.exporter = JsonResultSaver()
    
    async def crawl(self):
        self.logger.info(f"Starting crawl with max depth: {self.max_depth}")
        try:
            timeout = aiohttp.ClientTimeout(total=self.timeout)
            async with aiohttp.ClientSession(timeout=timeout) as session:
                for base_url in self.base_urls:
                    to_visit = {base_url}
                    for depth in range(self.max_depth):
                        self.logger.info(
                            f"Base URL: {base_url}, Depth: {depth}, "
                            f"Crawling {len(to_visit)} URLs..."
                        )
                        current_batch = list(to_visit)
                        to_visit.clear()
                        
                        tasks = [
                            self.fetcher.fetch(session, url)
                            for url in current_batch
                            if url not in self.visited_urls[base_url]
                        ]
                        self.visited_urls[base_url].update(current_batch)
                        
                        results = await asyncio.gather(*tasks)
                        extracted_links = []
                        for html in results:
                            if html:
                                extracted_links.extend(self.parser.parse_links(html))
                        
                        valid_links = self.filter.filter_urls(base_url, extracted_links)
                        to_visit.update(valid_links)
                
                self.logger.info("Crawling completed.")
        except Exception as e:
            self.logger.error(f"Error during crawl: {e}")
    
    def get_results(self):
        """
        Returns internal tracking structure as a dictionary.
        """
        return {base: list(urls) for base, urls in self.visited_urls.items()}
    
    def save_results(self):
        """
        Saves the results via the injected saver.
        """
        results_dict = self.get_results()
        self.exporter.save(results_dict)