# pip install beautifulsoup4 lxml
import re

from bs4 import BeautifulSoup

with open('blank/index.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
title = soup.title

# <title>Главная страница блога</title>
# print(title)

# Главная страница блога
# print(title.text, title.string)

# .find() .find_all()

# <h1>Страница пользователя Mr. Anderson</h1>
# find_h1 = soup.find('h1')
# print(find_h1)

# [<h1>Страница пользователя Mr. Anderson</h1>, <h1>Еще один h1 заголовок</h1>]
# find_h1_all = soup.find_all('h1')
# print(find_h1_all)

# user_name = soup.find('div', class_='user__name')
# print(user_name)

# user_name = soup.find('div', class_='user__name').find('span')
# print(user_name)

# user_name = soup.find('div', {'class': "user__birth__date", "id": "aaa"}).find('span')
# print(user_name.text)

# find_all_spans_in_user_info = soup.find('div', {'class': 'user__info'}).find_all('span')
# print(find_all_spans_in_user_info)


# fnd_social = soup.find('div', class_='social__networks').find_all('a')
# for item in fnd_social:
#     item_url = item.get('href')
#     print(item.text, item_url)

# .find_parent() .find_parents()

# post_div = soup.find(class_='post__text').find_parent('div', {'class':'user__post'})
# print(post_div)

# post_div = soup.find(class_='post__text').find_parents('div', 'user__post')
# print(post_div)

# .next_element .previous_element
# next_el = soup.find(class_='post__title').next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_='post__title').next_element.next_element
# print(next_el)


# .find_next_sibling(), .find_previous_sibling


# next_sib = soup.find(class_='post__title').find_next_sibling()
# print(next_sib)

find_a_by_a_text = soup.find_all(string=re.compile("([Oо]дежда)"))
print(find_a_by_a_text)