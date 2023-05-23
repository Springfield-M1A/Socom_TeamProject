import os
from django.shortcuts import render


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