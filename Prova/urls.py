from django.contrib import admin
from django.urls import path
from .views import listar, informar, atualizar, excluir

app_name = 'Prova'

urlpatterns = [
    path('', listar, name='informar_rendimento'),
    path('informar', informar, name='informar'),
    path('atualizar', atualizar, name='atualizar'),
    path('excluir', excluir, name='excluir')
]
