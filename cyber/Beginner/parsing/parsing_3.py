import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://en.wikipedia.org/wiki/Inub%C5%8Dsaki_Marine_Park"
response = requests.get(url)
soup = bs(response.text, "lxml")

for item in soup.find_all("a"):
    print(item.get("href"))