from bs4 import BeautifulSoup as bs
import requests

url = "https://uryupinka.ru/"
response = requests.get(url)
soup = bs(response.text, "lxml")
#print(soup)

with open("data.html", "w") as file:
    file.write(str(soup))

for item in soup.find_all("h2", class_="article-title"):
    print(item.text)