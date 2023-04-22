import requests
from bs4 import BeautifulSoup

# URL = https://kr.investing.com/equities/south-korea 종목 : KOSPI 100
response_URL = requests.get("https://api.investing.com/api/financialdata/assets/equitiesByIndices/49660?fields-list=id%2Cname%2Csymbol%2Chigh%2Clow%2Clast%2ClastPairDecimal%2Cchange%2CchangePercent%2Cvolume%2Ctime%2CisOpen%2Curl%2Cflag%2CcountryNameTranslated%2CexchangeId%2CperformanceDay%2CperformanceWeek%2CperformanceMonth%2CperformanceYtd%2CperformanceYear%2Cperformance3Year%2CtechnicalHour%2CtechnicalDay%2CtechnicalWeek%2CtechnicalMonth%2CavgVolume%2CfundamentalMarketCap%2CfundamentalRevenue%2CfundamentalRatio%2CfundamentalBeta&country-id=&page=0&page-size=0&include-major-indices=false&include-additional-indices=false&include-primary-sectors=false&include-other-indices=false&limit=0")

html = response_URL.text
print(html)

soup = BeautifulSoup(html, 'html.parser')
# 거래량 = data-test 특성
rates = soup.select('[data-test=volume-cell]')
for rate in rates:
    print(rate)

# 01시43분 크롤링 결과 equitiesByIndices/{숫자} 숫자 변화
def stock_crawler(market, page):
    url = f"https://api.investing.com/api/financialdata/assets/equitiesByIndices/49661?fields-list=id%2Cname%2Csymbol%2Chigh%2Clow%2Clast%2ClastPairDecimal%2Cchange%2CchangePercent%2Cvolume%2Ctime%2CisOpen%2Curl%2Cflag%2CcountryNameTranslated%2CexchangeId%2CperformanceDay%2CperformanceWeek%2CperformanceMonth%2CperformanceYtd%2CperformanceYear%2Cperformance3Year%2CtechnicalHour%2CtechnicalDay%2CtechnicalWeek%2CtechnicalMonth%2CavgVolume%2CfundamentalMarketCap%2CfundamentalRevenue%2CfundamentalRatio%2CfundamentalBeta&country-id=&page=0&page-size=0&include-major-indices=false&include-additional-indices=false&include-primary-sectors=false&include-other-indices=false&limit={page}"
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
    if input_Page >= 0:
        if input_page := 0:
            print('모든 페이지 출력')
            break
        else:
            break
    else:
        print('Page 입력 오류')

print("순서: '시간', '종목이름', '종가', '고가', '저가', '변동%' '거래량'")
# 함수 호출 테스트
print(stock_crawler(input_Market, input_Page))