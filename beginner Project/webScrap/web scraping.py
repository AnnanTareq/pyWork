import requests
from bs4 import BeautifulSoup

url = 'https://www.rokomari.com/pre-order?ref=sm_p7'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.content,'xml')
title = soup.find_all('p', {'class' : 'book-title'})

title_set = set()
for t in title:
    title_set.add(t.getText())

print(title_set)


