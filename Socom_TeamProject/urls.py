from django.urls import path
from .views import index, stock, prediction, beginner, copyrights
from stockapp import views
from stockapp.views import get_stock_data
from stockapp.views import stock_view

urlpatterns = [
    path('', index, name='index'),
    path('stock.html', stock, name='stock'),
    path('prediction.html', prediction, name='prediction'),
    path('beginner.html', beginner, name='beginner'),
    path('copyrights.html', copyrights, name='copyrights'),
    path('stock/', views.stock_view, name='stock'),
    path('api/stock/', views.get_stock_data, name='api_stock'),
]
