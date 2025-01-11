import logging

class Logger:
    """Reusable logger for the web crawler."""
    def __init__(self, name="web_crawler"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Avoid duplicate handlers
        if not self.logger.hasHandlers():
            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)
            console_formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            console_handler.setFormatter(console_formatter)

            # Add handlers
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger