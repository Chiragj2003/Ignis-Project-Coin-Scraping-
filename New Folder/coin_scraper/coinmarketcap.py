# coin_scraper/coinmarketcap.py
import requests
from bs4 import BeautifulSoup
import logging

class CoinMarketCap:
    @staticmethod
    def scrape_coin_data(coin_acronym):
        url = f"https://coinmarketcap.com/currencies/{coin_acronym.lower()}/"
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            coin_data = {}

            try:
                # Find elements containing the required data
                price_element = soup.find('div', class_='priceValue___11gHJ')
                price_change_element = soup.find('span', class_='icon-Caret-up')
                market_cap_element = soup.find('div', class_='statsValue___2iaoZ')
                market_cap_rank_element = soup.find('p', class_='statsCaption___3vaay')
                volume_element = soup.find('div', class_='statsValue___2iaoZ', text='Volume / Market Cap')
                volume_rank_element = soup.find('p', class_='statsCaption___3vaay', text='Trading Volume Rank')
                circulating_supply_element = soup.find('div', class_='statsValue___2iaoZ', text='Circulating Supply')
                total_supply_element = soup.find('div', class_='statsValue___2iaoZ', text='Total Supply')
                diluted_market_cap_element = soup.find('div', class_='statsValue___2iaoZ', text='Diluted Market Cap')

                # Extract data from elements
                coin_data['price'] = price_element.text.strip() if price_element else None
                coin_data['price_change'] = price_change_element.text.strip() if price_change_element else None
                coin_data['market_cap'] = market_cap_element.text.strip().replace(',', '') if market_cap_element else None
                coin_data['market_cap_rank'] = market_cap_rank_element.next_sibling.text.strip() if market_cap_rank_element else None
                coin_data['volume'] = volume_element.find_next_sibling('div', class_='statsValue___2iaoZ').text.strip().replace(',', '') if volume_element else None
                coin_data['volume_rank'] = volume_rank_element.next_sibling.text.strip() if volume_rank_element else None
                coin_data['circulating_supply'] = circulating_supply_element.find_next_sibling('div', class_='statsValue___2iaoZ').text.strip().replace(',', '') if circulating_supply_element else None
                coin_data['total_supply'] = total_supply_element.find_next_sibling('div', class_='statsValue___2iaoZ').text.strip().replace(',', '') if total_supply_element else None
                coin_data['diluted_market_cap'] = diluted_market_cap_element.find_next_sibling('div', class_='statsValue___2iaoZ').text.strip().replace(',', '') if diluted_market_cap_element else None
                
                # Log the scraped data
                logging.info(f"Scraped data for coin {coin_acronym}: {coin_data}")

            except Exception as e:
                # Log errors
                logging.error(f"Error occurred while scraping data for coin {coin_acronym}: {e}")
                # Set all data to None in case of error
                coin_data = {key: None for key in ['price', 'price_change', 'market_cap', 'market_cap_rank', 'volume', 'volume_rank', 'circulating_supply', 'total_supply', 'diluted_market_cap']}

            return coin_data
        
        else:
            return None
