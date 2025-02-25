'''

'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from fake_useragent import UserAgent
import time
import random

ua = UserAgent()


def setup_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(f"user-agent={ua.random}")
    options.add_argument("--window-size=1920x1080")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    return driver

def get_page(url):
    driver = setup_driver()
    driver.get(url)


    time.sleep(6)

    page = driver.page_source
    driver.quit()

    return page

def parse_page(page):
    soup = BeautifulSoup(page, 'html.parser')

    print(soup.prettify())

    products = []
    product_elem = soup.find_all('div', {'data-index': True})

    print(f"Found {len(product_elem)} products.")

    for product in product_elem:
        name = product.find('span', {'class': 'ds-text ds-text_lineClamp_2 ds-text_weight_med ds-text_color_text-primary ds-text_typography_lead-text ds-text_lead-text_normal ds-text_lead-text_med ds-text_lineClamp'})
        name = name.get_text() if name else 'Not found'
    
        products.append({
            'price': price
        })
    
    return products

def save_to_csv(page):
    df = pd.DataFrame(page)
    df.to_csv('yandex.csv', index=False)

def main():

    url = "https://market.yandex.ru/catalog--smartfony/16814639/list?hid=91491&glfilter=16816262:16816264&onstock=1"


    
    page = get_page(url)
    product = parse_page(page)
    save_to_csv(product)

if __name__ == '__main__':
    main()
