from django.contrib import admin
from django.urls import path, include
from .views import getPagamento, postPagamento

app_name = 'Atividade1'

urlpatterns = [
    path('', getPagamento, name='getPagamento'),
    path('post', postPagamento, name='postPagamento'),
    path('verificacao', getPagamento, name='getPagamento'),
]
