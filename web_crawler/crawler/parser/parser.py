import logging
from html import unescape

from bs4 import BeautifulSoup

from web_crawler.crawler.parser.interface import IHtmlParser


class BeautifulSoupParser(IHtmlParser):
    """Concrete parser using BeautifulSoup."""
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def parse_links(self, html: str) -> list:
        if not html:
            return []

        try:
            soup = BeautifulSoup(html, "html.parser")
            links = [unescape(a["href"]) for a in soup.find_all("a", href=True)]
            self.logger.debug(f"Found {len(links)} links")
            return links
        except Exception as e:
            self.logger.error(f"Error parsing HTML: {e}")
            return []