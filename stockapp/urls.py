from django.urls import path
from stockapp import views

urlpatterns = [
    path('prediction/', views.index),
]