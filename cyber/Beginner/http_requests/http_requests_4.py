import requests
import json

source_code = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = source_code.json()
print(f'Currencu of JPY {data['rates']['JPY']}')
