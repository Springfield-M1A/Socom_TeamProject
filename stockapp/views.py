import matplotlib.pyplot as plt
from django.shortcuts import render, HttpResponse
import pandas as pd
import requests
import os

def market_crawler(market):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize=30&page=1"
    response = requests.get(url)
    data = response.json()
    market_df = pd.DataFrame(data)
    market_df = market_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]
    return market_df

def code_crawler(code):
    url = f"https://m.stock.naver.com/api/stock/{code}/price?pageSize=30&page=1"
    response = requests.get(url)
    data = response.json()
    code_df = pd.DataFrame(data)
    code_df = code_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]
    return code_df

def stock_graph(market, code):
    market_df = market_crawler(kospi)
    market_price = market_df['closePrice']

    code_df = code_crawler(kosdaq,page)
    code_price = code_df['closePrice']

    market_price = market_price.str.replace(',', '').astype(float)
    code_price = code_price.str.replace(',', '').astype(float)

    plt.figure(figsize=(5, 2.5))

    x_market = market_df['localTradedAt']
    x_market = x_market[::-1]
    y_market = market_price.to_list()

    x_code = code_df['localTradedAt']
    x_code = x_code[::-1]
    y_code = code_price.to_list()


    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)

    plt.plot(x_market, y_market, label=market)

    plt.plot(x_code, y_code, label=code)
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
            <select name="stock">
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


