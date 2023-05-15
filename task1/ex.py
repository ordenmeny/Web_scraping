# задача: парсинг таблиц по категориям с данными. Сохранение каждой категории(данных этой категории) происходит в отдльный csv файл.

import requests
from bs4 import BeautifulSoup
import json

url = "https://calorizator.ru/product"

headers = {
    'Accept': "*/*",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}
req = requests.get(url, headers=headers)
src = req.text

# Сохранение страницы, на которой представлены категории
with open('index.html', 'w', encoding='utf-8') as file:
    file.write(src)

# Чтение страницы с категориями
with open('index.html', encoding='utf-8') as file:
    src = file.read()

# Получение ссылок на каждую категорию
soup = BeautifulSoup(src, 'lxml')
all_products_href = soup.find_all('ul', {'class': 'product'})

# запись ссылок на каждую категорию в словарь
all_cat_dict = {}
for el in all_products_href:
    for item in el.find_all('a'):
        all_cat_dict[item.text] = f'https://calorizator.ru/{item["href"]}'


# загрузка словаря в Json
with open('all_cat_dict.json', 'w', encoding='utf-8') as file:
    json.dump(all_cat_dict, file, indent=4, ensure_ascii=False)

