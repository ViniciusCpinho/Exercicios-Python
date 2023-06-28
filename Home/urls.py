from django.contrib import admin
from django.urls import path, include
from .views import Home, login 

urlpatterns = [
    path('', Home, name='home'),
    path('login', login, name='login'),
]
