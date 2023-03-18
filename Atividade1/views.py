from django.shortcuts import render
from .models import Pagamento


def getPagamento(request):
    pagamento = Pagamento.objects.all()
    return render(request, 'Atividade1_Index.html', {'pagamentos': pagamento})


def postPagamento(request):
    if (request.method == 'POST'):
        nome = request.POST.get('nome')
        quantidade_horas = request.POST.get('quantidade_horas')
        turno = request.POST.get('turno')
        categoria = request.POST.get('categoria')

        try:
            quantidade_horas = float(quantidade_horas)
            assert quantidade_horas >= 0
            assert categoria in ['Gerente', 'Operario']
            assert turno in ['Matutino', 'Vespetino', 'Noturno']
        except (ValueError, AssertionError):
            return render(request, 'form.html', {'error': 'Parâmetros inválidos'})

        # valorTotal:float; valorHora:float
        valor = verificacaoPagamento(quantidade_horas, categoria, turno)
        valorTotal = valor[0]
        valorHora = valor[1]

        # valorTotal = valor[0]
        # valorHora = valor[1]

        Pagamento.objects.create(
            nome=nome,
            quantidade_horas=quantidade_horas,
            turno=turno,
            categoria=categoria,
            valorTotal=valorTotal,
            valorHora=valorHora,
        )

        pagamento = Pagamento.objects.all()
        return render(request, 'Atividade1_index.html', {'pagamentos': pagamento, 'valo': valor})
    else:
        return render(request, 'form.html')


def verificacaoPagamento(quantidade_horas, categoria, turno):
    if categoria == 'Gerente' and turno == 'Noturno':
        valorHora = (1320 - 10/100) * 1.0
        valorTotal = valorHora * quantidade_horas
        return (valorTotal, valorHora)

    if categoria == 'Gerente' and (turno == 'Matutino' or turno == 'Vespetino'):
        valorHora = (1320 - 15/100) * 1.0
        valorTotal = valorHora * quantidade_horas
        return (valorTotal, valorHora)

    if categoria == 'Operario' and turno == 'Noturno':
        valorHora = (1320 - 9/100) * 1.0
        valorTotal = valorHora * quantidade_horas
        return (valorTotal, valorHora)

    # retorna uma tupla vazia caso nenhuma das condições acima seja satisfeita
    return ()
