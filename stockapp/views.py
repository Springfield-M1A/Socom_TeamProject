import matplotlib.pyplot as plt
from django.shortcuts import render, HttpResponse
import pandas as pd
import requests
import os

market='KOSPI'



def stock_crawler(market):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize=50&page=1"
    response = requests.get(url)
    data = response.json()
    market_df = pd.DataFrame(data)
    market_df = market_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]
    return market_df

def stock_crawler2(code):
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    requests = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    html=BeautifulSoup(requests.text, 'lxml')
    code_df = pd.concat([df, pd.read_html(requests.text, encoding='euc-kr')[0]], ignore_index=True)

    code_df.dropna(inplace=True)
    code_df.reset_index(drop=True, inplace=True)

def stock_graph(market):
    market_df = stock_crawler(market)
    market_price = market_df['closePrice']

    market_price = market_price.str.replace(',', '').astype(float)
    plt.figure(figsize=(5, 2.5))

    x_market = market_df['localTradedAt']
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


