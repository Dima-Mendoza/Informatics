import codecs
import csv
import os
import requests

retries = 0
wbHeaders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
    'Referer': 'https://www.wildberries.ru/',
    'Origin': 'https://www.wildberries.ru'
}

def flatten(categories):
    items = [item for item in categories['data']]
    res = []
    while len(items) > 0:
        item = items.pop()
        if (item.get('nodes')):
            items = items + item['nodes']
        res.append(item)
    return res

def parseProducts(products):
    items = products['data']['products']
    return [{"price": item['sizes'][0]['price']['total'], "name": item['name'], "rating": item['rating']} for item in items]

def fetchCategories():
    try:
        data = requests.get(f'https://catalog.wb.ru/menu/v11/api?locale=ru&lang=ru', headers=wbHeaders)
        json = data.json()
        return json, None
    except Exception as err:
        return None, err

def fetchProducts(category, cat):
    try:
        data = requests.get(f'https://catalog.wb.ru/catalog/{category}/v2/catalog?ab_testing=false&appType=1&cat={cat}&curr=rub&dest=-1257786&lang=ru&page=1&sort=pricedown&spp=30', headers=wbHeaders)
        json = data.json()
        return json, None
    except Exception as err:
        return None, err

def handle():
    categories, err = fetchCategories()
    global retries
    if err != None:
        if retries < 3:
            retries += 1
            print(f'Unable to fetch categories, retry {retries}...')
            handle()
            return
        else:
            print(f'Retry failed, shutting down...')
            return
    if os.path.isfile('records.csv'):
        os.remove('records.csv')
    writtenRows = 0
    flattenCategories = flatten(categories)
    with codecs.open('records.csv', 'a', "utf-8") as csvfile:
        fieldnames = ['price', 'name', 'rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(flattenCategories)):
            item = flattenCategories[i]
            products, err = fetchProducts(item['shardKey'], item['id'])
            if err != None:
                continue
            parsed = parseProducts(products)
            writtenRows += len(parsed)
            writer.writerows(parsed)
    print(f'Successfully written {writtenRows} to the records.csv')
    return

if __name__ == '__main__':
    handle()