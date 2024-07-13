import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CoinMarketCap:
    def __init__(self):
        self.driver = webdriver.Chrome()  # Replace with your preferred browser

    def scrape_data(self, coin):
        url = f'https://coinmarketcap.com/currencies/{coin}/'
        self.driver.get(url)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cmc-details-container')))
        data = {}
        data['price'] = self.driver.find_element_by_css_selector('.cmc-price').text
        data['price_change'] = self.driver.find_element_by_css_selector('.cmc-price-change').text
        data['market_cap'] = self.driver.find_element_by_css_selector('.cmc-market-cap').text
        data['market_cap_rank'] = self.driver.find_element_by_css_selector('.cmc-market-cap-rank').text
        data['volume'] = self.driver.find_element_by_css_selector('.cmc-volume').text
        data['volume_rank'] = self.driver.find_element_by_css_selector('.cmc-volume-rank').text
        data['volume_change'] = self.driver.find_element_by_css_selector('.cmc-volume-change').text
        data['circulating_supply'] = self.driver.find_element_by_css_selector('.cmc-circulating-supply').text
        data['total_supply'] = self.driver.find_element_by_css_selector('.cmc-total-supply').text
        data['diluted_market_cap'] = self.driver.find_element_by_css_selector('.cmc-diluted-market-cap').text
        contracts = []
        for contract in self.driver.find_elements_by_css_selector('.cmc-contract'):
            contracts.append({'name': contract.find_element_by_css_selector('.cmc-contract-name').text, 'address': contract.find_element_by_css_selector('.cmc-contract-address').text})
        data['contracts'] = contracts
        official_links = []
        for link in self.driver.find_elements_by_css_selector('.cmc-official-link'):
            official_links.append({'name': link.find_element_by_css_selector('.cmc-official-link-name').text, 'link': link.find_element_by_css_selector('.cmc-official-link-url').get_attribute('href')})
        data['official_links'] = official_links
        socials = []
        for social in self.driver.find_elements_by_css_selector('.cmc-social'):
            socials.append({'name': social.find_element_by_css_selector('.cmc-social-name').text, 'url': social.find_element_by_css_selector('.cmc-social-url').get_attribute('href')})
        data['socials'] = socials
        return data

    def close(self):
        self.driver.quit()