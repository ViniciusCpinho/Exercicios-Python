from django.contrib import admin
from django.urls import path
from .views import getElevadores, postElevadores
from . import views 

app_name = 'Atividade2'


urlpatterns = [
    path('', getElevadores, name='getElevadores'),
    path('post', postElevadores, name='postElevadores'),
    path('home', views.Home, name='Home')

]
