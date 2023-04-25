import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL = https://kr.investing.com/equities/south-korea 종목 : KOSPI 100
response_URL = requests.get("https://kr.investing.com/equities/south-korea")
html = response_URL.text
soup = BeautifulSoup(html, 'html.parser')
print(html)
# 거래량 = data-test 특성
rates = soup.select('.datatable_cell__0y0eu datatable_cell--align-end__fwomz dynamic-table_col-other__tKGpI')
for rate in rates:
    print(rate)
print('-----------------')

# 01시43분 크롤링 결과 equitiesByIndices/{숫자} 숫자 변화
def stock_crawler(market, page, pageSize):
    url = f"https://api.investing.com/api/financialdata/assets/equitiesByIndices/49661?fields-list=id%2Cname%2Csymbol%2Chigh%2Clow%2Clast%2ClastPairDecimal%2Cchange%2CchangePercent%2Cvolume%2Ctime%2CisOpen%2Curl%2Cflag%2CcountryNameTranslated%2CexchangeId%2CperformanceDay%2CperformanceWeek%2CperformanceMonth%2CperformanceYtd%2CperformanceYear%2Cperformance3Year%2CtechnicalHour%2CtechnicalDay%2CtechnicalWeek%2CtechnicalMonth%2CavgVolume%2CfundamentalMarketCap%2CfundamentalRevenue%2CfundamentalRatio%2CfundamentalBeta&country-id=&page={page}&page-size={pageSize}&include-major-indices=false&include-additional-indices=false&include-primary-sectors=false&include-other-indices=false&limit=0"
    response = requests.get(url)
    data = response.json()
    market_df = pd.DataFrame(data)
    return market_df[['Time', 'Name', 'Last', 'High', 'Low','PerformanceDay', 'Volume']]
print('함수 입력, 호출 (KOSPI, KOSDAQ)')

while True:
    input_Market = input('Market: ')
    if input_Market == 'KOSPI' or input_Market == 'KOSDAQ':
        break
    else:
        print('Market 입력 오류')

while True:
    input_Page = int(input('Page: '))
    if input_Page > 0:
        break
    else:
        print('Page 입력 오류')

while True:
    input_PageSize = int(input('PageSize: '))
    if input_PageSize > 0:
        break
    else:
        print('PageSize 입력 오류')

print("순서: '시간', '종목이름', '종가', '고가', '저가', '변동%' '거래량'")
# 함수 호출 테스트
print(stock_crawler(input_Market, input_Page, input_PageSize))