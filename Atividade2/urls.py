from django.contrib import admin
from django.urls import path
from .views import getElevadores, updateElevadores

app_name = 'Atividade2'


urlpatterns = [
    path('', getElevadores, name='getElevadores'),
    path('update', updateElevadores, name='updateElevadores'),
]
