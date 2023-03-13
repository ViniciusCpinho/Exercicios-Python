from django.shortcuts import render
from .models import Atividades


def Home(request):
    atividade = Atividades.objects.all()
    return render(request, 'index.html', {'atividades': atividade})
