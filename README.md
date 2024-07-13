# Bit Coin Scraper

This project is a web scraper for Coin Scraper that uses Selenium to gather various details about a specified cryptocurrency. The details include price, market cap, volume, circulating supply, total supply, and related contract addresses, among others.

## Prerequisites

- Python 3.x
- Selenium
- Fast API
- WebDriver for your preferred browser (e.g., ChromeDriver for Chrome)

## Installation

1. Clone the repository:

    ```sh
    https://github.com/Chiragj2003/Ignis-Project-Coin-Scraping-.git
    cd CoinMarketCapScraper
    ```

2. Install the required Python packages:

    ```sh
    pip install selenium
    ```

## Usage

1. Import the `CoinMarketCap` class:

    ```python
    from coinmarketcap import CoinMarketCap
    ```

2. Create an instance of the `CoinMarketCap` class:

    ```python
    scraper = CoinMarketCap()
    ```

3. Scrape data for a specific cryptocurrency:

    ```python
    data = scraper.scrape_data('bitcoin')  # Replace 'bitcoin' with the desired cryptocurrency slug
    print(data)
    ```

4. Close the scraper when done:

    ```python
    scraper.close()
    ```

## Example

Here's a full example:

```python
from coinmarketcap import CoinMarketCap

# Create a scraper instance
scraper = CoinMarketCap()

# Scrape data for Bitcoin
data = scraper.scrape_data('bitcoin')

# Print the scraped data
print(data)

# Close the scraper
scraper.close()
