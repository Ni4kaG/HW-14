import pprint

import requests
from bs4 import BeautifulSoup

url ='https://dedmorozural.ru/novosti'
result = requests.get(url)
# print(result.status_code)
soup = BeautifulSoup(result.text, 'html.parser')
# print(soup.title)
# print(type(soup.title))
# # через точку находим только первый тег
# print(soup.a)
# print(soup.a.string)
# print( soup.a.get('href'))

# как найти все теги картинок
# img_tags = soup.find_all('img')
# for img_tag in img_tags:
#     print(img_tag)

# !!!!поиск по классу
big_body_tag = soup.find('div', class_= 'modulebody1')
# print(big_body_tag)

modulebody3 = big_body_tag.find('div', class_='modulebody3')
print(big_body_tag.contents[1])
print(modulebody3.a)
# здесь только дети без внуков
# for child in big_body_tag.children:
#     print(1)
#     print(child)
# здесь все вложенные дети

print(len(list(big_body_tag.children)))
print(len(list(big_body_tag.descendants)))

# for child in big_body_tag.descendants:
#     print(0)
#     print(child)