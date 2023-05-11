from django.shortcuts import render, redirect
import os
import csv


# Create your views here.

APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(APP_DIR, 'Files')
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
FILE_PATH = os.path.join(BASE_DIR, 'Rendimentos.txt')

erro = 'Não há arquivos registrados'

meses = {'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6, 
         'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12}


def listar(request):
    try:
        with open(FILE_PATH, 'r') as f:
            reader = csv.reader(f, delimiter=' ')
            numLine = sum(1 for row in reader)
            data = [{
                'mes': row[0],
                'ano': row[1],
                'salario': row[2],
                'despesa': row[3],
                'saldo': row[4],
                'investimento': row[5],
                'rendimento': 'Bateu a meta' if int(row[4]) == int(row[2]) * 0.1 * numLine else 'Não bateu a meta'
            } for row in reader]
            return render(request, 'index_prova.html', {'dados':data})
    except FileNotFoundError:
        return render(request, 'index_prova.html', {'dados': erro})

def informar(request):
    if(request.method == 'POST'):
        mes = request.POST.get('mes', '')
        ano = request.POST.get('ano', '')
        salario = request.POST.get('salario', 'Não informado')
        despesa = request.POST.get('despesa', 'Não informado')
        
        try:
            salario = int(salario)
            despesa = int(despesa)
            saldo = salario - despesa
            investimento = saldo * 10 / 100
            if saldo < 0:
                data = 'Não foi possível salvar'
                return render(request, 'index_prova.html', {'dados':data})
            data = f'{mes} {ano} {salario} {despesa} {saldo} {investimento}\n'
            with open(FILE_PATH, '+a') as file:
                file.write(data)
            return redirect('Prova:informar_rendimento')
        except ValueError:
            data = 'Não é um salário válido'
            return render(request, 'index_prova.html', {'dados':data})
    else:
        return redirect('Prova:informar_rendimento')
    
def atualizar(request):
    if request.method == 'POST':
        mes_antigo = request.POST.get('mes_antigo', '')
        ano_antigo = request.POST.get('ano_antigo', '')
        mes_novo = request.POST.get('mes_novo', '')
        ano_novo = request.POST.get('ano_novo', '')
        tipo= request.POST.get('tipo_novo')
        quantidade_novo = request.POST.get('quantidade', '')
                
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
        for i in range(len(lines)):
            mes, ano, salario, despesa, saldo, investimento = lines[i].split()
            if mes == mes_antigo and ano == ano_antigo: 
                if tipo == 'salario':
                    lines[i] = f'{mes_novo} {ano_novo} {quantidade_novo} {despesa} {investimento}\n'
                else:
                    lines[i] = f'{mes_novo} {ano_novo} {salario} {quantidade_novo} {investimento}\n'
                break    
        with open(FILE_PATH, 'w') as file:
            file.writelines(lines)

    return redirect('Prova:informar_rendimento')
      
def excluir(request):
    if request.method == 'POST':
        mes = request.POST.get('mes')
        ano = request.POST.get('ano')
        
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
        
        with open(FILE_PATH, 'r+') as file:
            for line in lines:
                mes_arquivo, ano_arquivo, *_ = line.split()
                if mes != mes_arquivo or ano != ano_arquivo:
                    file.write(line)
                                 
    return redirect('Prova:informar_rendimento')