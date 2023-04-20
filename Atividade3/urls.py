from django.contrib import admin
from django.urls import path
from .views import get_arquivo, post_arquivo, Home

app_name= 'Atividade3'

urlpatterns = [
    path('', get_arquivo, name='get_arquivo'),
    path('post', post_arquivo, name='post_arquivo'),
    path('home', Home, name='home')
]
