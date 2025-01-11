import json

from web_crawler.crawler.exporter.interface import IResultSaver


class JsonResultSaver(IResultSaver):
    """Concrete saver to JSON file."""
    def __init__(self, filename="data/results.json"):
        self.filename = filename

    def save(self, results):
        """Saves results as JSON to a specified filename."""
        with open(self.filename, "w") as f:
            json.dump(results, f, indent=4)