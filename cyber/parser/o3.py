import time
import csv
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
import pandas as pd

from fake_useragent import UserAgent

# -------- Настройки --------
# Путь к драйверу ChromeDriver (или другой драйвер, если используете Firefox/Edge и т.д.)
CHROMEDRIVER_PATH = r"/usr/bin/chromedriver"

# URL страницы со смартфонами и телефонами на Ozon
URL = "https://www.ozon.ru/category/smartfony-i-telefony-15502/"

# Имя CSV-файла для конечных результатов
CSV_FILENAME = "ozon_phones.csv"

# Количество скроллов вниз (зависит от того, сколько товаров нужно получить)
SCROLL_COUNT = 5

# Количество попыток при ошибках (пример, как можно обрабатывать сбои)
RETRY_COUNT = 3

# Количество товаров, которое мы хотим собрать (не менее 100 в условии)
TARGET_COUNT = 100


def init_webdriver():
    """
    Инициализация Selenium WebDriver с подменой User-Agent
    """
    ua = UserAgent()
    user_agent = ua.random  # Получаем рандомный User-Agent

    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    #chrome_options.add_argument("--headless")  # Если нужно запускать браузер в фоновом режиме, без интерфейса
    # При необходимости можно добавить и другие аргументы

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def scroll_down(driver, scroll_count):
    """
    Прокрутка страницы вниз для подгрузки товаров.
    """
    for _ in range(scroll_count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Небольшая пауза, чтобы контент успел подгрузиться


def parse_page(driver):
    """
    Сбор данных о товарах с уже прокрученной страницы.
    Возвращает список словарей с данными.
    """
    soup = BeautifulSoup(driver.page_source, "html.parser")
    items_data = []

    # Класс/селектор может меняться, поэтому нужно смотреть актуальную HTML-разметку
    product_cards = soup.find_all("div", attrs={"style": "grid-area: tile; position: relative;"})
    
    for card in product_cards:
        try:
            # Название
            title_tag = card.find("div", {"class": "bq016-a bq016-a4 bq016-a6 j1j_24"})  
            title = title_tag.text.strip() if title_tag else "Название не найдено"

            # Ссылка на товар
            link = None
            if title_tag and title_tag.get("href"):
                link = "https://www.ozon.ru" + title_tag.get("href")

            # Цена
            price_block = card.find("span", {"class": "c3024-a1 tsHeadline500Medium c3024-b1 c3024-a6"})
            price = price_block.text.strip() if price_block else "Цена не найдена"

            # Рейтинг (иногда может не быть на карточке)
            rating_block = card.find("span", {"class": "k3y3j0"})
            rating = rating_block.text.strip() if rating_block else "Рейтинг отсутствует"

            # Характеристики (примерно; зависит от текущей верстки)
            # Можно в идеале переходить по ссылке на страницу товара и вытягивать характеристики детально.
            # Здесь упрощенно берём часть описания с карточки
            characteristics = []
            chars_container = card.find("div", {"class": "ui-k6 ui-k7"})
            if chars_container:
                for char_item in chars_container.find_all("li"):
                    characteristics.append(char_item.text.strip())
            
            items_data.append({
                "Название": title,
                "Цена": price,
                "Рейтинг": rating,
                "Ссылка": link,
                "Характеристики": "; ".join(characteristics)
            })
        except Exception as e:
            print(f"Ошибка при парсинге одной из карточек: {e}")

    return items_data


def save_to_csv(data, filename):
    """
    Сохранение списка словарей в CSV-файл через pandas.
    """
    df = pd.DataFrame(data)
    # Режим "a" (append) и header=False используется, если файл уже существует (промежуточное сохранение)
    write_header = not os.path.exists(filename)
    df.to_csv(filename, mode='a', index=False, header=write_header, encoding="utf-8")


def main():
    # Инициализация Selenium
    driver = init_webdriver()

    # Счётчик попыток
    attempts = 0

    # Промежуточные результаты
    all_data = []

    while attempts < RETRY_COUNT:
        try:
            # Переходим на страницу каталога
            driver.get(URL)
            time.sleep(3)

            # Скроллим страницу
            scroll_down(driver, SCROLL_COUNT)

            # Парсим данные
            parsed_data = parse_page(driver)
            all_data.extend(parsed_data)

            print(f"Собрано товаров на данном этапе: {len(all_data)}")
            
            # Сохраняем промежуточный результат, чтобы не потерять при сбоях
            save_to_csv(parsed_data, CSV_FILENAME)
            print(f"Промежуточное сохранение в {CSV_FILENAME} завершено.")

            # Если собрали уже нужное кол-во товаров, выходим
            if len(all_data) >= TARGET_COUNT:
                print(f"Достигнут лимит в {TARGET_COUNT} товаров. Завершаем парсинг.")
                break

            # Если не достигли лимита, но крутить дальше особо некуда, попробуем ещё раз
            # (В реальном проекте можно перейти на следующую страницу, кликнуть «Показать ещё» и т.п.)
            attempts += 1
            print(f"Попытка {attempts}/{RETRY_COUNT} закончена. Повторим для проверки наличия новых данных...")

        except Exception as e:
            print(f"Ошибка: {e}")
            attempts += 1
            time.sleep(5)  # Небольшая задержка перед повтором

    driver.quit()

    # После выхода из цикла сохраняем результат окончательно (на случай, если не хватило 100 товаров)
    if all_data:
        print(f"Всего собрано товаров: {len(all_data)}. Результат в файле {CSV_FILENAME}")
    else:
        print("Не удалось собрать данные о товарах.")


if __name__ == "__main__":
    main()