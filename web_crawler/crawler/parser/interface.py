class IHtmlParser:
    """Interface for parsing HTML content."""
    def parse_links(self, html: str) -> list:
        """Returns a list of extracted links (strings)."""
        raise NotImplementedError