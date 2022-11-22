# pip install beautifulsoup4 
# pip install requests
import re
from bs4 import BeautifulSoup
import requests

url = 'https://vk.com/_group'

page = requests.get(url)

print(page.status_code)


filteredNews = []
allNews = []

soup = BeautifulSoup(page.text, "html.parser")
# print(soup)
allNews = soup.findAll(class_='pi_text')
print(f'All News text: {allNews}')

for data in allNews:
    if data.find(class_='pi_text') is not None:
        filteredNews.append(data.text)

for data in filteredNews:
    print(data)

print('_'*10)
print(filteredNews)

# def remove_html_tags(text):
#     """Remove html tags from a string"""
#     clean = re.compile('<.*?>')
#     return re.sub(clean, '', text)

# final_text = remove_html_tags(data)
# print(final_text)