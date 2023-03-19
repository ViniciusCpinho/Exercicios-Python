from django.shortcuts import render, redirect
from .models import Pagamento
from Home import views

#Pega os dados do banco
def getPagamento(request):
    pagamento = Pagamento.objects.all()
    return render(request, 'Atividade1_Index.html', {'pagamentos': pagamento})


def postPagamento(request):
    #Verifica a request
    if (request.method == 'POST'):
        nome = request.POST.get('nome')
        quantidade_horas = request.POST.get('quantidade_horas')
        turno = request.POST.get('turno')
        categoria = request.POST.get('categoria')

        #Verifica se as respostas são as dentro do esperado
        try:
            quantidade_horas = float(quantidade_horas)
            assert quantidade_horas >= 0
            assert categoria in ['Gerente', 'Operario']
            assert turno in ['Matutino', 'Vespetino', 'Noturno']
            
        #Se não estiver dentro do padrão é mandado erro o user para o template novamente
        except (ValueError, AssertionError):
            return render(request, 'form.html', {'error': 'Parâmetros inválidos'})

        valor = verificacaoPagamento(quantidade_horas, categoria, turno)
        valorTotal = valor[0]
        valorHora = valor[1]

        Pagamento.objects.create(
            nome=nome,
            quantidade_horas=quantidade_horas,
            turno=turno,
            categoria=categoria,
            valorTotal=valorTotal,
            valorHora=valorHora,
        )

        return redirect('Atividade1:getPagamento')
    
    #Manda novamente para o template
    else:
        return render(request, 'form.html')

#Define o valor total e o valor da hora
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
    
    if categoria == 'Operario' and (turno == 'Matutino' or turno == 'Vespetino'):
        valorHora = (1320 - 14/100) * 1.0
        valorTotal = valorHora * quantidade_horas
        return (valorTotal, valorHora)



def Home(request):
    return redirect(views.Home)