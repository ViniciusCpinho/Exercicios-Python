from django.contrib import admin
from django.urls import path
from .views import getCountries

app_name = 'Atividade4',

urlpatterns = [
    path('', getCountries, name='getCountries'),
]
