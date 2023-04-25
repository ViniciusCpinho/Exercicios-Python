from django.shortcuts import render, redirect
import os

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
        if os.path.getsize(FILE_PATH) == 0:
            return render(request, 'index_prova.html', {'files': erro})
        else:
            files = open(FILE_PATH, 'r')
            files_line = files.readlines()
            
            data = []
            for folha_rendimento in files_line:
                mes, ano, salario, despesa, saldo, investimento = folha_rendimento.split()
                rendimento = (int(salario) * 10 / 100) * 0.1 * len(files_line)
                if rendimento == int(saldo) * 0.1 * len(files_line):
                    rendimento == 'Bateu a meta'
                else: 
                    rendimento == 'Não bateu a meta'
                    
                data.append({
                    'mes': mes,
                    'ano': ano,
                    'salario': salario,
                    'despesa': despesa,
                    'saldo': saldo,
                    'investimento': investimento,
                    'rendimento': rendimento
                })
            return render(request, 'index_prova.html', {'dados':data})
    except FileNotFoundError:
        return render(request, 'index_prova.html', {'dados': erro})

def informar(request):
    if(request.method == 'POST'):
        mes = request.POST.get('mes', '')
        ano = request.POST.get('ano', '')
        salario = request.POST.get('salario', 'Não informado')
        despesa = request.POST.get('despesa', 'Não informado')
        saldo = int(salario) - int(despesa)
        
        if(salario < despesa):
            data = 'o salário não pode ser menor que a despesa'
            return render(request, 'index_prova.html', {'dados':data})
        
        else:
            if saldo < 0: 
                data = 'Não foi possivel salvar'
                return render(request, 'index_prova.html', {'dados':data})
            else:
                try:
                    investimento = int(saldo) * 10/100
                except:
                    data = 'Não é um salário valido'
                    return render(request, 'index_prova.html', {'dados':data})
                data = f'{mes} {ano} {salario} {despesa} {saldo} {investimento}\n'        
                
                with open(FILE_PATH, '+a') as file:
                    file.write(data)

                return redirect('Prova:informar_rendimento')
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
                if tipo == 'despesa':
                    lines[i] = f'{mes_novo} {ano_novo} {salario} {quantidade_novo} {investimento}\n'
                if tipo == 'salario':
                    lines[i] = f'{mes_novo} {ano_novo} {quantidade_novo} {despesa} {investimento}\n'
                if tipo == 'ambos':
                    lines[i] = f'{mes_novo} {ano_novo} {quantidade_novo} {despesa} {investimento}\n'
                break
        with open(FILE_PATH, 'w') as file:
                file.writelines(lines)
        
        return redirect('Prova:informar_rendimento')
    else:
        return redirect('Prova:informar_rendimento')
    
def excluir(request):
    if request.method == 'POST':
        mes = request.POST.get('mes')
        ano = request.POST.get('ano')
    
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
        new_lines = []
        for line in lines:
            mes_arquivo, ano_arquivo, salario, despesa, saldo, investimento = line.split()
            if mes == mes_arquivo and ano == ano_arquivo:
                continue
            else:
                new_lines.append(line)
        with open(FILE_PATH, 'w') as file:
            file.writelines(new_lines)
    return redirect('Prova:informar_rendimento')
