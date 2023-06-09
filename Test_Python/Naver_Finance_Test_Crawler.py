from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://finance.naver.com/sise/sise_market_sum.nhn?page=1"

res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')

print (soup)

stock_head = soup.find("thead").find_all("th")
data_head = [head.get_text() for head in stock_head]

print(data_head)

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