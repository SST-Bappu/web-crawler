# Web Crawler 

This repository demonstrates a basic web crawler to discover product URL.  
It breaks down the components of a crawler (fetching, parsing, filtering, and storing results) into single-purpose classes and interfaces to ensure modularity, flexibility, and maintainability.

---

## Table of Contents

- [Overview](#overview)  
- [Project Structure](#project-structure)  
- [Key Components](#key-components)
  - [Logging (`Logger`)](#logging-logger)  
  - [Fetcher (`AsyncHtmlFetcher`)](#fetcher-asynchtmlfetcher)  
  - [Parser (`BeautifulSoupParser`)](#parser-beautifulsoupparser)  
  - [URL Filtering (`DefaultUrlFilter`)](#url-filtering-defaulturlfilter)  
  - [Result Saving (`JsonResultSaver`)](#result-saving-jsonresultsaver)  
  - [Crawler (`Crawler`)](#crawler-crawler)  
- [How to Use](#how-to-use)  
- [Extending the Crawler](#extending-the-crawler)  
- [License](#license)

---

## Overview

This crawler uses asynchronous HTTP requests (with `aiohttp`), parses the returned HTML to extract links (with BeautifulSoup), filters out unwanted or invalid URLs, and saves the final results to a JSON file. By leveraging SOLID principles, each step of the process is self-contained and can be easily swapped out for a different implementation.

### SOLID Principles in Action

1. **Single Responsibility**: Each class handles a specific part of the crawling process.  
2. **Open/Closed**: The crawler supports adding or replacing fetchers, parsers, filters, and savers by implementing the respective interfaces.  
3. **Liskov Substitution**: Any class that follows the `IHtmlFetcher`, `IHtmlParser`, `IUrlFilter`, or `IResultSaver` interface can be substituted at runtime without breaking the crawler.  
4. **Interface Segregation**: Each interface has minimal methods focusing on one piece of functionality (e.g., fetching, parsing, saving).  
5. **Dependency Inversion**: The `Crawler` depends on interfaces rather than concrete implementations.

---

## Project Structure

## Key Components

### Logging (`Logger`)

- **Purpose**: Provides a standardized logger (based on Python’s built-in logging).  
- **Class**: `Logger`  
- **Usage**:
  ```python
  logger_instance = Logger("MyCrawler").get_logger()
  logger_instance.info("Starting the crawler...")


### Fetcher (`AsyncHtmlFetcher`)

- **Purpose**: Fetch HTML data from a given URL using `aiohttp`.  
- **Interface**: `IHtmlFetcher` defines the contract.
- **Class**: `AsyncHtmlFetcher` is the concrete implementation.
- **Usage**:
  ```python
  fetcher = AsyncHtmlFetcher(logger_instance)


### Parser (`BeautifulSoupParser`)

- **Purpose**: Parse HTML content and extract links.  
- **Interface**: `IHtmlParser` defines the contract.
- **Class**: `BeautifulSoupParser` is the concrete implementation using BeautifulSoup.
- **Usage**:
  ```python
  parser = BeautifulSoupParser(logger_instance)

### URL Filtering (`DefaultUrlFilter`)

- **Purpose**: Validate extracted URLs and convert relative paths to absolute URLs.  
- **Interface**: `IUrlFilter` defines the contract.
- **Class**: `DefaultUrlFilter` is the concrete implementation.
- **Usage**:
  ```python
  url_filter = DefaultUrlFilter(logger_instance)

### Result Saving (`JsonResultSaver`)

- **Purpose**: Persist results to a JSON file.  
- **Interface**: `IResultSaver` defines the contract.
- **Class**: `JsonResultSaver` is the concrete implementation.
- **Usage**:
  ```python
  saver = JsonResultSaver("data/results.json")


### Crawler (`Crawler`)

- **Purpose**: Orchestrate the entire crawling process by:
  - Setting up an async session
  - Iterating through URLs up to the configured depth
  - Fetching, parsing, filtering links
  - Storing results using the injected saver

- **Class**: `Crawler`

- **Constructor Arguments**:
  - `fetcher` (implements `IHtmlFetcher`)
  - `parser` (implements `IHtmlParser`)
  - `url_filter` (implements `IUrlFilter`)
  - `saver` (implements `IResultSaver`)
  - `logger` (any Python logger instance)



## How to Use

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

2. **Instantiate Components and Run the crawler**
   ```python
   start_urls = ["list of urls"]
    crawler = WebCrawler(start_urls, max_depth=2)
    
    
    async def main():
        await crawler.crawl()
        crawler.save_results()



3. **Check Results**
  The crawler stores results in the `data/results.json` file. The JSON contains a dictionary mapping each base URL to a list of discovered URLs.



## Extending the Crawler

Because of the modular, interface-based design, you can easily add or swap components:

- **Fetcher**: Implement a new class extending `IHtmlFetcher` if you want to use a different HTTP library or add caching.
- **Parser**: Implement a new `IHtmlParser` if you need a different parsing logic (e.g., regex-based or advanced HTML5 parsing).
- **URL Filter**: Implement a new `IUrlFilter` for more sophisticated filtering rules.
- **Result Saver**: Implement a new `IResultSaver` to store results in a database, CSV file, or an in-memory structure instead of JSON.

Just initialize these into the `Crawler` constructor, and you’re ready to go without modifying the core crawler logic.
