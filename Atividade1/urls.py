from django.contrib import admin
from django.urls import path, include
from .views import getPagamento, postPagamento
from . import views 

app_name = 'Atividade1'

urlpatterns = [
    path('', getPagamento, name='getPagamento'),
    path('post', postPagamento, name='postPagamento'),
    path('home', views.Home, name='Home')
]
