from django.urls import path, include
from .views import index, stock, prediction, beginner, copyrights
from stockapp import views
from . import views
app_name = 'stockapp'

urlpatterns = [
    path('', index, name='index'),
    path('stock.html', stock, name='stock'),
    path('prediction/', include('stockapp.urls')),
    path('beginner.html', beginner, name='beginner'),
    path('copyrights.html', copyrights, name='copyrights'),
]