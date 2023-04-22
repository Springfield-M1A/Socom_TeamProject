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
