from django.shortcuts import render, redirect
from .models import Elevadores
from Home import views

#Pega os dados do banco de dados, realiza analise dos dados e manda para o template 
def getElevadores(request):
    elevadores = Elevadores.objects.all()
    respostas = analises(elevadores)
    
    return render(request, 'Atividade2_Index.html', {'respostas': respostas})
    
#Salva os dados dentro do banco de dados
def postElevadores(request):
    if (request.method == 'POST'):
        elevador = request.POST.get('elevador')
        turno = request.POST.get('turno')

        #Verificação se os dados estão colocados corretos
        try:
            assert elevador in ['A', 'B', 'C']
            assert turno in ['Matutino', 'Vespetino', 'Noturno']
            
        #Não corretos envia erro e retorna para o mesmo template 
        except (ValueError, AssertionError):
            return render(request, 'form2.html', {'error': 'Parâmetros inválidos'})

        Elevadores.objects.create(
            elevador = elevador,
            turno = turno,
        )
        
        return redirect('Atividade2:getElevadores')

    
    #Caso não seja post retorna o template
    else:
        return render(request, 'form2.html')


#Realiza o processo de analise dos dados
def analises(elevadores):
    
    # Inicializa o dicionário que irá armazenar as análises
    respostas = {   'A': {'Matutino': 0, 'Vespetino': 0, 'Noturno': 0},
                    'B': {'Matutino': 0, 'Vespetino': 0, 'Noturno': 0},
                    'C': {'Matutino': 0, 'Vespetino': 0, 'Noturno': 0},                    
                    }
    
    # Variáveis para as análises das questões c, d e e
    elevador_mais_utilizado = None
    elevador_mais_utilizado_total = 0
    periodo_mais_utilizado = None
    periodo_mais_utilizado_total = 0
    periodo_total = 0
    periodo_menos_utilizado = None
    periodo_menos_utilizado_total = float('inf')
    
    # Faz a análise dos dados
    for elevador in elevadores:
        elevador_str = elevador.elevador
        turno_str = elevador.turno
        respostas[elevador_str][turno_str] += 1
        
        # Análise para a questão c
        if respostas[elevador_str][turno_str] > elevador_mais_utilizado_total:
            elevador_mais_utilizado_total = respostas[elevador_str][turno_str]
            elevador_mais_utilizado = elevador_str + '-' + turno_str
        
        # Análise para as questões d e e
        periodo_total += 1
        periodo_mais_utilizado_total_atual = respostas[elevador_str][turno_str]
        if periodo_mais_utilizado_total_atual > periodo_mais_utilizado_total:
            periodo_mais_utilizado_total = periodo_mais_utilizado_total_atual
            periodo_mais_utilizado = turno_str
        if periodo_mais_utilizado_total_atual < periodo_menos_utilizado_total:
            periodo_menos_utilizado_total = periodo_mais_utilizado_total_atual
            periodo_menos_utilizado = turno_str
    
    # Calcula a diferença percentual para a questão e
        diferenca_percentual = (((periodo_mais_utilizado_total/periodo_total) * 100)
                                - ((periodo_menos_utilizado_total/periodo_total)* 100))

    
    # Adiciona as análises das questões c, d e e ao dicionário respostas
    respostas['Elevador_mais_utilizado'] = elevador_mais_utilizado
    respostas['Periodo_mais_utilizado'] = periodo_mais_utilizado
    respostas['Diferenca_percentual'] = diferenca_percentual
    
    # Retorna o dicionário com as análises
    return respostas

def Home(request):
    return redirect(views.Home)