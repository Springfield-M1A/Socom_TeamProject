from django.shortcuts import render, HttpResponse
import pandas as pd
import requests

market='KOSPI'
pageSize=10
page=0

def stock_crawler(market, pageSize, page):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize={pageSize}&page={page}"
    response = requests.get(url)
    data = response.json()
    market_df = pd.DataFrame(data)
    return market_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]

def prediction(request):
    market = 'KOSPI'
    pageSize = 10
    page = 0

    if request.GET:
        market = request.GET.get('market', market)
        pageSize = int(request.GET.get('pageSize', pageSize))
        page = int(request.GET.get('page', page))

    if not request.GET:
        result = "market='KOSPI', pageSize='10', page='0'"
    else:
        result = f"market='{market}', pageSize='{pageSize}', page='{page}'"

    # 여기에 그래프, 표 넣기

    html_response = f"""
        <p>{result}</p>
        
        <a href="https://www.ktb.co.kr/trading/popup/itemPop.jspx" target="_blank"><img src="../static/images/Code.png" alt="코드 종목 조회"></a>
        <p></p>
        <form action="">
            <input type="text" name="market" placeholder="종목 코드 입력">
            <select name="pageSize">
                <option value="5">30</option>
                <option value="10">60</option>
                <option value="20">120</option>
                <option value="30">180</option>
                <option value="40">240</option>
            </select>
            <input type="submit" value="조회">
        </form>

    """

    return HttpResponse(html_response)
