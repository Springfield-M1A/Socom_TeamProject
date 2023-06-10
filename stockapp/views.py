import matplotlib.pyplot as plt
from django.shortcuts import render, HttpResponse
import pandas as pd
import requests
import os

def stock_crawler(stock):
    url = f"https://m.stock.naver.com/api/index/{stock}/price?pageSize=30&page=1"
    response = requests.get(url)
    data = response.json()
    stock_df = pd.DataFrame(data)
    stock_df = stock_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]
    return stock_df

def code_crawler(code):
    url = f"https://m.stock.naver.com/api/stock/{code}/price?pageSize=30&page=1"
    response = requests.get(url)
    data = response.json()
    code_df = pd.DataFrame(data)
    code_df = code_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]
    return code_df

def stock_graph(kospi, kosdaq, page):
    stock_df = stock_crawler(kospi,page)
    stock_price = stock_df['closePrice']

    code_df = code_crawler(kosdaq,page)
    code_price = code_df['closePrice']

    stock_price = stock_price.str.replace(',', '').astype(float)
    code_price = code_price.str.replace(',', '').astype(float)

    plt.figure(figsize=(5, 2.5))

    x_market = kospi_df['localTradedAt']
    x_market = x_market[::-1]
    y_market = market_price.to_list()

    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    plt.plot(x_market, y_market, label=market)
    plt.legend(loc=0)

    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    image_path = os.path.join(static_dir, 'images', 'graph.png')

    plt.savefig(image_path)




def prediction(request):
    market = 'KOSPI'

    if request.GET:
        market = request.GET.get('market', market)

    # 여기에 그래프, 표, 예측 넣기
    graph=stock_graph(market)


    html_response = f"""
    <div class="container">
        <a href="https://www.ktb.co.kr/trading/popup/itemPop.jspx" target="_blank"><img src="../static/images/Code.png" alt="코드 종목 조회"></a>
        <p></p>
        <form action="">
            <select name="market">
                <option value="KOSPI">KOSPI</option>
                <option value="KOSDAQ">KOSDAQ</option>
            </select>
            
            <input type="text" name="code" placeholder="종목코드">
            <input type="submit" value="조회">
        </form>
        </div>
        
        <div class="graph" style="width:400px height:300px">
        <img src="../static/images/graph.png" alt="그래프">
    </div>

    """

    return HttpResponse(html_response)


