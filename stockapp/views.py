import matplotlib.pyplot as plt
from django.shortcuts import render, HttpResponse
from sklearn import preprocessing
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

def stock_graph(market, code, normalization):
    market_df = market_crawler(market)
    market_price = market_df['closePrice']
    market_price = market_price.str.replace(',', '').astype(float)

    if (code != ''):
        code_df = code_crawler(code)
        code_price = code_df['closePrice']
        code_price = code_price.str.replace(',', '').astype(float)



    plt.figure(figsize=(5, 2.5))

    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)


    x_market = market_df['localTradedAt']
    x_market = x_market[::-1]
    y_market = market_price.to_list()
    y_market_normalization = preprocessing.minmax_scale(y_market)

    if (normalization == 'True'):
        plt.plot(x_market, y_market_normalization, label=market)
    else:
        plt.plot(x_market, y_market, label=market)


    if (code != ''):
            x_code = code_df['localTradedAt']
            x_code = x_code[::-1]
            y_code = code_price.to_list()
            y_code_normalization = preprocessing.minmax_scale(y_code)

            if (normalization == 'True'):
                plt.plot(x_code, y_code_normalization, label=code)
            else:
                plt.plot(x_code, y_code, label=code)

    plt.legend(loc=0)

    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    image_path = os.path.join(static_dir, 'images', 'graph.png')

    plt.savefig(image_path)




def prediction(request):
    market = 'KOSPI'
    code = ''

    if request.GET:
        market = request.GET.get('market', market)
        code = request.GET.get('code', code)

    # 여기에 그래프, 표, 예측 넣기
    graph=stock_graph(market, code, normalization)


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
            <select name="normalization">
                <option value="False">기본</option>
                <option value="True">정규화</option>
            </select>
            
            <input type="submit" value="조회">
        </form>
        </div>
        
        <div class="graph" style="width:400px height:300px">
        <img src="../static/images/graph.png" alt="그래프">
    </div>

    """

    return HttpResponse(html_response)


