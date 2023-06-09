import matplotlib.pyplot as plt
from django.shortcuts import render, HttpResponse
import pandas as pd
import requests

market='KOSPI'
pageSize=10
page=1

def stock_crawler(market, pageSize, page):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize={pageSize}&page={page}"
    response = requests.get(url)
    data = response.json()
    market_df = pd.DataFrame(data)
    market_df = market_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]
    return market_df

def stock_graph(market, pageSize, page):
    market_df = stock_crawler(market, pageSize, page)
    market_price = market_df['closePrice']

    market_price = market_price.str.replace(',', '').astype(float)
    plt.figure(figsize=(20, 10))

    x_market = market_df['localTradedAt']
    y_market = market_price.to_list()

    plt.plot(x_market, y_market, label=market)
    plt.legend(loc=0)
    plt.savefig('graph.png')


def prediction(request):
    market = 'KOSPI'
    pageSize = 10
    page = 1

    if request.GET:
        market = request.GET.get('market', market)
        pageSize = int(request.GET.get('pageSize', pageSize))
        page = int(request.GET.get('page', page))

    if not request.GET:
        result = "market='KOSPI', pageSize='10', page='0'"
        graph=stock_graph(market, pageSize, page)
    else:
        result = f"market='{market}', pageSize='{pageSize}', page='{page}'"
        graph=stock_graph(market, pageSize, page)

    # 여기에 그래프, 표, 예측 넣기
    graphpath = 'graph.png'




    html_response = f"""
        <p>{result}</p> <!-- 나중에 삭제 -->
        
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
        <img src="{graphpath}" alt="그래프">


    """

    return HttpResponse(html_response)


