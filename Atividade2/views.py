from django.shortcuts import render, redirect
from .models import Elevadores

def getElevadores(request):
    elevadores = Elevadores.objects.all()
    respostas = analises(elevadores)
    
    return render(request, 'Atividade2_Index.html', {'respostas': respostas})
    
def postElevadores(request):
    if (request.method == 'POST'):
        elevador = request.POST.get('elevador')
        turno = request.POST.get('turno')

        try:
            assert elevador in ['A', 'B', 'C']
            assert turno in ['Matutino', 'Vespetino', 'Noturno']
        except (ValueError, AssertionError):
            return render(request, 'form2.html', {'error': 'Parâmetros inválidos'})

        Elevadores.objects.create(
            elevador = elevador,
            turno = turno,
        )
        
        return redirect('Atividade2:getElevadores')

            
    else:
        return render(request, 'form2.html')
    
def analises(elevadores):
    
    # Inicializa o dicionário que irá armazenar as análises
    respostas = {'A': {'Matutino': 0, 'Vespetino': 0, 'Noturno': 0},
                     'B': {'Matutino': 0, 'Vespetino': 0, 'Noturno': 0},
                     'C': {'Matutino': 0, 'Vespetino': 0, 'Noturno': 0}}
    
    # Faz a análise dos dados
    for elevador in elevadores:
        elevador_str = elevador.elevador
        turno_str = elevador.turno
        respostas[elevador_str][turno_str] += 1
    
    # Retorna o dicionário com as análises
    return respostas