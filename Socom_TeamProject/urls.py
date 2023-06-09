from django.urls import path
from .views import index, stock, prediction, beginner, copyrights
from stockapp import views
from predictionapp import views
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('stock.html', stock, name='stock'),
    path('predictionapp.url', prediction, name='prediction'),
    path('beginner.html', beginner, name='beginner'),
    path('copyrights.html', copyrights, name='copyrights'),
]