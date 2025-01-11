import logging
from urllib.parse import urlparse, urljoin

from web_crawler.crawler.filters.interface import IUrlFilter


class DefaultUrlFilter(IUrlFilter):
    """Concrete filter implementation."""
    
    def __init__(self, logger: logging.Logger):
        self.logger = logger
    
    def filter_urls(self, base_url: str, urls: list) -> list:
        valid_urls = []
        for url in urls:
            if not url:
                continue
            url = url.strip()
            # ignore JavaScript or anchor links
            if url.startswith("javascript") or url.startswith("#") or url.startswith("mailto"):
                continue
            # convert relative to absolute
            if not urlparse(url).netloc:
                url = urljoin(base_url, url)
            valid_urls.append(url)
        
        self.logger.debug(f"Filtered valid URLs: {valid_urls}")
        return valid_urls
