class IUrlFilter:
    """Interface for filtering and normalizing URLs."""
    def filter_urls(self, base_url: str, urls: list) -> list:
        """Returns filtered & normalized URLs (absolute, etc.)."""
        raise NotImplementedError