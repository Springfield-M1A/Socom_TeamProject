from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://m.stock.naver.com/")

bs0bject = BeautifulSoup(html, "html.parser")

for link in bs0bject.find_all('img'):
    print(link.text.strip(), link.get('src'))