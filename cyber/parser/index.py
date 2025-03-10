import codecs
import csv
import os
import requests

HEADERS = {
    'User-Agent': 'Opera/9.80 (Windows NT 6.1; WOW64) Presto/2.12.388 Version/12.18',
    'Referer': 'https://www.wildberries.ru/',
    'Origin': 'https://www.wildberries.ru'
}

def extract_categories(categories):
    stack = categories['data'][:]
    result = []
    
    while stack:
        item = stack.pop()
        if 'nodes' in item:
            stack.extend(item['nodes'])
        result.append(item)
    
    return result

def process_products(products):
    return [
        {
            "Стоимость товара": round(item['sizes'][0]['price']['total'] / 100, 2),
            "Название  товара": item['name'],
            "Рейтинг товара": item['rating'] if item['rating'] > 0 else "-"
        }
        for item in products.get('data', {}).get('products', [])
    ]

def get_categories():
    try:
        response = requests.get('https://catalog.wb.ru/menu/v11/api?locale=ru&lang=ru', headers=HEADERS)
        response.raise_for_status()
        return response.json(), None
    except requests.RequestException as err:
        return None, err

def get_products(category_key, category_id):
    url = f'https://catalog.wb.ru/catalog/{category_key}/v2/catalog?ab_testing=false&appType=1&cat={category_id}&curr=rub&dest=-1257786&lang=ru&page=1&sort=pricedown&spp=30'
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json(), None
    except requests.RequestException as err:
        return None, err

def run_parser(retries=0, max_retries=3):
    categories, err = get_categories()
    
    if err:
        if retries < max_retries:
            print(f'Ошибка при получении категорий, попытка {retries + 1}/{max_retries}...')
            return run_parser(retries=retries + 1)
        else:
            print('Не удалось получить категории. Завершение работы.')
            return
    
    if os.path.isfile('data.csv'):
        os.remove('data.csv')
    
    written_rows = 0
    flat_categories = extract_categories(categories)
    
    with codecs.open('data.csv', 'a', "utf-8") as csvfile:
        fieldnames = ['Стоимость товара', 'Название  товара', 'Рейтинг товара']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for category in flat_categories:
            products, err = get_products(category['shardKey'], category['id'])
            if err:
                print(f'Ошибка при получении товаров для категории {category["name"]}, пропуск...')
                continue
            
            parsed_products = process_products(products)
            written_rows += len(parsed_products)
            writer.writerows(parsed_products)
    
    print(f'Успешно записано {written_rows} строк в data.csv')

if __name__ == '__main__':
    run_parser()
