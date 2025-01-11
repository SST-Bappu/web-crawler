import logging

from web_crawler.crawler.fetcher.interface import IHtmlFetcher


class AsyncHtmlFetcher(IHtmlFetcher):
    """Concrete fetcher using aiohttp."""
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    async def fetch(self, session, url: str) -> str:
        self.logger.info(f"Fetching URL: {url}")
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    self.logger.info(f"Successfully fetched: {url}")
                    return await response.text()
                else:
                    self.logger.warning(f"Failed to fetch {url}, Status: {response.status}")
        except Exception as e:
            self.logger.error(f"Failed to fetch: {url} - {e}")
            return ''

        return ''