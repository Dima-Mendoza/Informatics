import requests
from bs4 import BeautifulSoup as bs
import csv

url = "https://technical.city/ru/video/rating"
response = requests.get(url)
soup = bs(response.text, "lxml")

data = []

for item in soup.find_all("img"):
    data.append(item.get("alt"))

print(data)

data[0] = "Name"

with open("data.csv", "w", newline="") as file:
        datawriter = csv.writer(file)
        datawriter.writerows(data)
#        for i in data:
#            datawriter.writerow(i)