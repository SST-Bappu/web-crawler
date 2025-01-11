class IHtmlFetcher:
    """Interface for fetching HTML."""
    async def fetch(self, session, url: str) -> str:
        """Returns HTML of the requested URL or None."""
        raise NotImplementedError