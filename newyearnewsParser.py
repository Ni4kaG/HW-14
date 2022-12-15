import pprint

import requests
from bs4 import BeautifulSoup
domain = 'https://dedmorozural.ru'
url =f'{domain}/novosti'
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

news_tag = soup.find_all('a', class_='con_titlelink')
result_news = {}
for a_news1 in news_tag:
    text = a_news1.text
    href = a_news1.get('href')
    url1 = f'{domain}{href}'
    response = requests.get(url1)
    soup1 = BeautifulSoup(response.text, 'html.parser')
    news1_title_tag = soup.find_all('strong')
    titles = []
    for title_tag in news1_title_tag:
        titles.append(title_tag.text)
    result_news[text] = titles
pprint.pprint(result_news)