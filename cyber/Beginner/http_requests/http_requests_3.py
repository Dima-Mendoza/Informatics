import requests

source_code = requests.get("https://google.com/").content
print(source_code)