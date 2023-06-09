import os
from django.shortcuts import render
from django.http import JsonResponse
import requests


from .models import Stock

def stock(request):
    # 상위 5개 종목 정보 가져오기
    top_stocks = Stock.objects.all()[:5]

    context = {
        'top_stocks': top_stocks
    }

    return render(request, 'stock.html', context)
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

