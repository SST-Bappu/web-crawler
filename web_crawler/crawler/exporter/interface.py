class IResultSaver:
    """Interface for saving results."""
    def save(self, results):
        """Save results somewhere."""
        raise NotImplementedError