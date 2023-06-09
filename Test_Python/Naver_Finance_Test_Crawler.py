from bs4 import BeautifulSoup
import requests
import pandas as pd

code='005930'
page=1

url = f"https://finance.naver.com/item/sise.naver?code={code}&page={page}"
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.text

soup = BeautifulSoup(html, 'html.parser')

price = soup.select_one("#_nowVal").text
print(price)

for page in range(1, 11):
    url = f"https://finance.naver.com/item/sise.naver?code={code}&page={page}"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')

    df = pd.concat([df, pd.read_html(html, encoding='euc-kr')[0]], ignore_index=True)

def stock_crawler(market):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize=50&page=1"
    response = requests.get(url)
    data = response.json()
    market_df = pd.DataFrame(data)
    market_df = market_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]
    return market_df