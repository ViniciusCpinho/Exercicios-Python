from django.shortcuts import render, redirect
from .models import Elevadores

def getElevadores(request):
    
    elevadores = Elevadores.objects.all()
    preferido_a = elevadores.filter(preferido='A').count()
    preferido_b = elevadores.filter(preferido='B').count()
    preferido_c = elevadores.filter(preferido='C').count()

    periodo_matutino = elevadores.filter(periodo='Matutino').count()
    periodo_vespertino = elevadores.filter(periodo='Vespertino').count()
    periodo_noturno = elevadores.filter(periodo='Noturno').count()

    total_elevadores = preferido_a + preferido_b + preferido_c
    total_periodos = periodo_matutino + periodo_vespertino + periodo_noturno

    if total_elevadores > 0:
        perc_preferido_a = (preferido_a / total_elevadores) * 100
        perc_preferido_b = (preferido_b / total_elevadores) * 100
        perc_preferido_c = (preferido_c / total_elevadores) * 100
    else:
        perc_preferido_a = perc_preferido_b = perc_preferido_c = 0

    periodos = {'Matutino': periodo_matutino, 'Vespertino': periodo_vespertino, 'Noturno': periodo_noturno}
    periodo_mais_usado = max(periodos, key=periodos.get)
    periodo_menos_usado = min(periodos, key=periodos.get)
    diferenca_percentual = abs(((periodos[periodo_mais_usado] - periodos[periodo_menos_usado]) / total_periodos) * 100)

    return render(request, 'Atividade2_Index.html', {
        'elevadores': elevadores,
        'preferido_a': preferido_a,
        'preferido_b': preferido_b,
        'preferido_c': preferido_c,
        'elevador_mais_utilizado': elevador_mais_utilizado,
        'periodo_mais_utilizado': periodo_mais_usado,
        'percent_mais_utilizado': periodos[periodo_mais_usado]/total_elevadores*100 if total_elevadores > 0 else 0,
        'periodo_menos_utilizado': periodo_menos_usado,
        'percent_menos_utilizado': periodos[periodo_menos_usado]/total_elevadores*100 if total_elevadores > 0 else 0,
        'diferenca_percentual': diferenca_percentual,
    })  

def postElevadores(request):
    if request.method == 'POST':
        preferido = request.POST.get('preferido')
        periodo = request.POST.get('periodo')

        try:
            assert preferido in ['A', 'B', 'C']
            assert periodo in ['Matutino', 'Vespetino', 'Noturno']
        except (ValueError, AssertionError):
            return render(request, 'form.html', {'error': 'Parâmetros inválidos'})

        elevador = Elevadores(preferido=preferido, periodo=periodo)
        elevador.save()

        return redirect('getElevadores')
    else:
        return render(request, 'form.html')



def updateElevadores(request):
    if request.method == 'POST':
        preferido = request.POST.get('preferido')
        periodo = request.POST.get('periodo')

        try:
            assert preferido in ['A', 'B', 'C']
            assert periodo in ['Matutino', 'Vespetino', 'Noturno']
        except (ValueError, AssertionError):
            return render(request, 'form2.html', {'error': 'Parâmetros inválidos'})

        ultimo_elevador = Elevadores.objects.last()

        if not ultimo_elevador:
            elevador = Elevadores(preferido=preferido, periodo=periodo)
            elevador.save()
        else:
            if ultimo_elevador.preferido == preferido and ultimo_elevador.periodo == periodo:
                ultimo_elevador.save()
            else:
                elevador = Elevadores(preferido=preferido, periodo=periodo)
                elevador.save()

        return redirect('getElevadores')
    else:
        return render(request, 'form2.html')

def calcularEstatisticas(elevadores):
    # Contagem de utilização dos elevadores por período
    count_a_m = elevadores.filter(preferido='A', periodo='M').count()
    count_a_v = elevadores.filter(preferido='A', periodo='V').count()
    count_a_n = elevadores.filter(preferido='A', periodo='N').count()

    count_b_m = elevadores.filter(preferido='B', periodo='M').count()
    count_b_v = elevadores.filter(preferido='B', periodo='V').count()
    count_b_n = elevadores.filter(preferido='B', periodo='N').count()

    count_c_m = elevadores.filter(preferido='C', periodo='M').count()
    count_c_v = elevadores.filter(preferido='C', periodo='V').count()
    count_c_n = elevadores.filter(preferido='C', periodo='N').count()

    # Cálculo da utilização total dos elevadores
    total_a = count_a_m + count_a_v + count_a_n
    total_b = count_b_m + count_b_v + count_b_n
    total_c = count_c_m + count_c_v + count_c_n

    # Cálculo do elevador mais utilizado
    if total_a > total_b and total_a > total_c:
        elevador_mais_utilizado = 'A'
    elif total_b > total_a and total_b > total_c:
        elevador_mais_utilizado = 'B'
    else:
        elevador_mais_utilizado = 'C'

    # Cálculo do período mais utilizado
    if count_m := count_a_m + count_b_m + count_c_m:
        periodo_mais_utilizado = 'M'
    elif count_v := count_a_v + count_b_v + count_c_v:
        periodo_mais_utilizado = 'V'
    else:
        periodo_mais_utilizado = 'N'

    percent_m = ((count_a_m + count_b_m + count_c_m) / total_periodos) * 100
    percent_v = ((count_a_v + count_b_v + count_c_v) / total_periodos) * 100
    percent_n = ((count_a_n + count_b_n + count_c_n) / total_periodos) * 100

    periodos = {'M': percent_m, 'V': percent_v, 'N': percent_n}
    periodo_mais_usado = max(periodos, key=periodos.get)
    periodo_menos_usado = min(periodos, key=periodos.get)
    diferenca_percentual = periodos[periodo_mais_usado] - periodos[periodo_menos_usado]

    # Renderização do template com os resultados
    return render(request, 'Atividade2_Index.html', {
        'elevadores': elevadores,
        'preferido_a': preferido_a,
        'preferido_b': preferido_b,
        'preferido_c': preferido_c,
        'elevador_mais_utilizado': elevador_mais_utilizado,
        'periodo_mais_utilizado': periodo_mais_utilizado,
        'percent_mais_utilizado': periodos[periodo_mais_usado],
        'periodo_menos_utilizado': periodo_menos_usado,
        'percent_menos_utilizado': periodos[periodo_menos_usado],
        'diferenca_percentual': diferenca_percentual,
    })

