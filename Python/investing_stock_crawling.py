import requests
from bs4 import BeautifulSoup
import datetime

current_time = datetime.datetime.now()
now_time = current_time.timestamp()
real_time=int(now_time)
#현재 시간 타임스템프

print("현재 타임스템프: ", real_time)
def past_time_search(input_told):
    old_time = datetime.datetime(input_told)
    past_time = old_time.timestamp()
    return past_time          
print("특정 시작 시간 입력")
pyear = input("시작 년도: ")
pmonth = input("시작 날짜(월): ")
pdays = input("시작 날짜(일): ")
phours = input("시작 시간(시): ")
pminties = input("시작 시간(분) ")
pseconds = input("시작 시간(초) ")
told = pyear + pmonth + pdays + phours + pminties + pseconds
past_time = past_time_search(told)
# 시작 시간을 입력 후 타임스템프로 변환
print(real_time)
print(past_time)
print('-----------------')

#URL = https://kr.investing.com/equities/south-korea 종목 : KOSPI 지수
url = f"https://tvc4.investing.com/474af0ef7f7ba36b8f73cf744ccebd3f/{real_time}/18/18/88/history?symbol=37426&resolution=D&from={past_time}&to={real_time}}"
response_URL = requests.get(url)
html = response_URL.text
soup = BeautifulSoup(html, 'html.parser')
print(html)
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