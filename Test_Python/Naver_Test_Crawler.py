import requests
import pandas as pd

market='KOSPI'
pageSize = 10
page = 1

url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize={pageSize}&page={page}"
print(url)

# 1차 Response 테스트
print('1차 Response 테스트')
response = requests.get(url)
print(response.text)
print('-----------------')

# 2차 Response 테스트 (json)
print('2차 Response 테스트 (json)')
data = response.json()
print(data)
print('-----------------')

# 3차 Response 테스트 (json -> DataFrame)
print('3차 Response 테스트 (json -> DataFrame)')
kospi_df = pd.DataFrame(data)

print(kospi_df)
print('-----------------')
print(kospi_df[['localTradedAt', 'closePrice', 'openPrice']])
print('-----------------')

# 4차 함수화 테스트
print('4차 함수화 테스트')
def stock_crawler(market, pageSize, page):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize={pageSize}&page={page}"
    response = requests.get(url)
    data = response.json()
    market_df = pd.DataFrame(data)
    return market_df[['localTradedAt', 'closePrice', 'openPrice']]

# 함수 입력 테스트
print('함수 입력, 호출 (KOSPI, KOSDAQ)')
while True:
    input_Market = input('Market: ')
    if input_Market == 'KOSPI' or input_Market == 'KOSDAQ':
        break
    else:
        print('Market 입력 오류')

while True:
    input_PageSize = int(input('PageSize: '))
    if input_PageSize > 0:
        break
    else:
        print('PageSize 입력 오류')

while True:
    input_Page = int(input('Page: '))
    if input_Page > 0:
        break
    else:
        print('Page 입력 오류')

# 함수 호출 테스트
print(stock_crawler(input_Market, input_PageSize, input_Page))