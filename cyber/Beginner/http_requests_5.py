import requests

try:
    user_inp = input(str("Please, enter url: "))
    source_code = requests.get(user_inp)
except requests.exceptions.ConnectionError as e:
    print(e)

print(user_inp)