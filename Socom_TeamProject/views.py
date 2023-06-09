import os
from django.shortcuts import render
from django.http import JsonResponse
import requests
# Create your views here.

ALPHA_VANTAGE_API_KEY = 'QM7BI9O6YE2M3M6M'

def stock(request):
    # 주식 정보 가져오기
    stocks = Stock.objects.all()  # Stock 모델의 모든 주식 정보를 가져옴

    # 필요한 데이터를 컨텍스트로 전달하여 stock.html 렌더링
    return render(request, 'stock.html', {'stocks': stocks})
def stock_view(request):
    return render(request, 'stock.html')

def get_stock_data(request):
    symbol = request.GET.get('symbol', 'AAPL')
    interval = request.GET.get('interval', 'daily')

    base_url = 'https://www.alphavantage.co/query?'
    function = 'TIME_SERIES_DAILY' if interval == 'day' else 'TIME_SERIES_MONTHLY'

    data = requests.get(f'{base_url}function={function}&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}').json()

    return JsonResponse(data)
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

