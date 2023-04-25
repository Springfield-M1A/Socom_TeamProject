import requests
from bs4 import BeautifulSoup

market = 'KOSPI'
pageSize = 10
page = 1

# URL = https://m.stock.naver.com/domestic/index/KOSPI/total  KOSPI 구성종목별 시세
response_URL = f"https://m.stock.naver.com/api/index/{market}/enrollStocks?pageSize={pageSize}&page={page}&type=object"
print(response_URL)
# response 테스트
response = requests.get(response_URL)
print(response.text)
print('-----------------')
