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
    return HttpResponse('''
        <a href="https://www.ktb.co.kr/trading/popup/itemPop.jspx" target="_blank"><img src="../static/images/Code.png" alt="코드 종목 조회"></a>
        <p></p>
        <form action="">
            <input type="text" name="market" placeholder="종목 코드 입력">
            <select name="pageSize">
                <option value="10">10</option>
                <option value="20">20</option>
                <option value="30">30</option>
                <option value="40">40</option>
                <option value="50">50</option>
            </select>
            <input type="submit" value="조회">
            
            <p>현재 market = {% market %}</p>
        </form>
    ''')
