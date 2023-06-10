import matplotlib.pyplot as plt
from django.shortcuts import render, HttpResponse
from sklearn import preprocessing
import pandas as pd
import requests
import os
import json
import numpy as np

def market_crawler(market):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize=30&page=1"
    response = requests.get(url)

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("No data to decode")
        data = {}

    market_df = pd.DataFrame(data)
    market_df = market_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]
    return market_df

def code_crawler(code):
    url = f"https://m.stock.naver.com/api/stock/{code}/price?pageSize=30&page=1"
    response = requests.get(url)

    try:
        data = response.json()
    except json.JSONDecodeError:
        print("No data to decode")
        data = {}

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

    plt.figure(figsize=(8, 4))

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

def coefficient(market, code):
    market_df = market_crawler(market)
    market_price = market_df['closePrice']
    market_price = market_price.str.replace(',', '').astype(float)

    if (code != ''):
        code_df = code_crawler(code)
        code_price = code_df['closePrice']
        code_price = code_price.str.replace(',', '').astype(float)
        y_code = code_price.to_list()
        y_code_normalization = preprocessing.minmax_scale(y_code)

    y_market = market_price.to_list()
    y_market_normalization = preprocessing.minmax_scale(y_market)

    if (code != ''):
        coef = np.corrcoef(y_market_normalization, y_code_normalization)[0, 1]*100
        answer = f"{market}와 {code} 의 상관계수는 {coef:.2f}% 입니다."
    else:
        answer = f"{code} 종목이 없어 {market} 와의 상관계수를 계산할 수 없습니다."

    return answer


def predict_prices(df, model_name, days=5):
    df = df[['localTradedAt', 'closePrice']]
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'])
    df['y'] = df['y'].astype(float)

    if model_name.lower() == 'arima':
        model = ARIMA(df['y'], order=(5,1,0))
        model_fit = model.fit(disp=0)
        forecast, stderr, conf_int = model_fit.forecast(steps=days)
    return forecast

def prediction_trend(forecast):
    trends = []
    for i in range(1, len(forecast)):
        if forecast[i] > forecast[i-1]:
            trends.append('↗')
        else:
            trends.append('↘')
    return trends

def stock_prediction(market, code):
    market_df = market_crawler(market)
    code_df = code_crawler(code)

    arima_forecast_market = predict_prices(market_df, 'arima')
    arima_trends_market = prediction_trend(arima_forecast_market)

    if (code != ''):
        arima_forecast_code = predict_prices(code_df, 'arima')
        arima_trends_code = prediction_trend(arima_forecast_code)

    result = {
        'arima_market': arima_trends_market,
        'arima_code': arima_trends_code,
    }

    return result

def prediction(request):
    market = 'KOSPI'
    code = ''
    normalization = 'False'

    if request.GET:
        market = request.GET.get('market', market)
        code = request.GET.get('code', code)
        normalization = request.GET.get('normalization', normalization)


    # 여기에 그래프, 표, 예측 넣기
    graph=stock_graph(market, code, normalization)
    answer=coefficient(market, code)
    stock_prediction_result = stock_prediction(market, code)

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
        <p> {answer} </p>
        
        <p>ARIMA 예측 (시장) : {' '.join(stock_prediction_result['arima_market'])}</p>
        <p>ARIMA 예측 (종목) : {' '.join(stock_prediction_result['arima_code'])}</p>
    </div>

    """

    return HttpResponse(html_response)


