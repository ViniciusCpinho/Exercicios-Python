from django.shortcuts import render
from .models import Paises

# Create your views here.

def getCountries(request):
    paises = Paises.objects.all()
    return render(request, 'AtividadeQuatro_Index.html', {'paises': paises})

def postCountries(request):
    nome_pais = request.POST.get('nome_pais')
    paises = Paises.objects.all()
    
    if(paises == []):
        for pais in paises: 
        Paises.objects.create(        
    )
