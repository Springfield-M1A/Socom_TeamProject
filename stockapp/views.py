import os
from django.shortcuts import render
from django.http import JsonResponse
from .forms import StockPredictionForm
import requests
import pandas as pd
def index(request):
    return render(request, 'index.html')

def stock(request):
    return render(request, 'stock.html')

def prediction(request):
    return render(request, 'prediction.html')

def beginner(request):
    return render(request, 'beginner.html')

def copyrights(request):
    return render(request, 'copyrights.html')

market='KOSPI'
pageSize=10
page=1

url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize={pageSize}&page={page}"

def stock_crawler(market, pageSize, page):
    url = f"https://m.stock.naver.com/api/index/{market}/price?pageSize={pageSize}&page={page}"
    response = requests.get(url)
    data = response.json()
    market_df = pd.DataFrame(data)
    return market_df[['localTradedAt', 'closePrice', 'compareToPreviousClosePrice', 'openPrice', 'highPrice', 'lowPrice']]

def stock_prediction(request):
    if request.method == 'POST':
        form = StockPredictionForm(request.POST)
        if form.is_valid():
            stock_name = form.cleaned_data['stock_name']
            page_size = form.cleaned_data['page_size']
            stock_data = []
            for page in range(0, 11):
                data = stock_crawler(stock_name, page_size, page)
                stock_data.extend(data)

            return render(request, 'prediction.html', {'form': form, 'stock_data': stock_data})
    else:
        form = StockPredictionForm()

    return render(request, 'prediction.html', {'form': form})
