import json
import csv
import requests
from bs4 import BeautifulSoup

# Чтение Json-файла для получения словаря из категрия->ссылка
with open('all_cat_dict.json', 'r', encoding='utf-8') as file:
    src = json.load(file)

headers = {
    'Accept': "*/*",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

for key, val in src.items():
    try:
        url = val

        req = requests.get(url, headers=headers)
        src = req.text
        with open(f'data/{key}.html', 'w', encoding='utf-8') as file:
            file.write(src)

        with open(f'data/{key}.html', encoding='utf-8') as file:
            src = file.read()

        soup = BeautifulSoup(src, 'lxml')

        head_table = soup.find('table', class_='views-table').find('thead').find_all('a')

        with open(f'data/{key}.csv', 'a', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(
                (
                    head_table[0].text,
                    head_table[1].text,
                    head_table[2].text,
                    head_table[3].text,
                    head_table[4].text,
                )
            )

        body_table_tr = soup.find('tbody').find_all('tr')

        for tr in body_table_tr:
            with open(f'data/{key}.csv', 'a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(
                    (tr.find_all('td')[1].text.strip().replace('\n', ''),
                     tr.find_all('td')[2].text.strip().replace('\n', ''),
                     tr.find_all('td')[3].text.strip().replace('\n', ''),
                     tr.find_all('td')[4].text.strip().replace('\n', ''),
                     tr.find_all('td')[5].text.strip().replace('\n', ''),
                     )
                )
    except:
        print("Ошибка!", key, val)

    print(key, val)

