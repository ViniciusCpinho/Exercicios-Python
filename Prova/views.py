from django.shortcuts import render, redirect
import os

# Create your views here.

APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(APP_DIR, 'Files')
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
FILE_PATH = os.path.join(BASE_DIR, 'Rendimentos.txt')

erro = 'Não há arquivos registrados'


def listar(request):
    try:
        if os.path.getsize(FILE_PATH) == 0:
            return render(request, 'index_prova.html', {'files': erro})
        else:
            files = open(FILE_PATH, 'r')
            files_line = files.readlines()
            
            data = []
            for folha_rendimento in files_line:
                mes, ano, dinheiro = folha_rendimento.split()
                data.append({
                    'mes': mes,
                    'ano': ano,
                    'dinheiro': dinheiro,
                })
            return render(request, 'index_prova.html', {'dados':data})
    except FileNotFoundError:
        return render(request, 'index_prova.html', {'dados': erro})

def informar(request):
    if(request.method == 'POST'):
        mes = request.POST.get('mes', '')
        ano = request.POST.get('ano', '')
        quantidade = request.POST.get('quantidade', '')
        tipo = request.POST.get('tipo', '')
        
        data = f'{mes} {ano} {quantidade} {tipo}\n'
        
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
        tipo_novo= request.POST.get('tipo_novo')
        quantidade = request.POST.get('quantidade', '')
        
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
        for i in range(len(lines)):
                mes, ano = lines[i].split()
                if mes == mes_antigo and ano == ano_antigo: 
                    lines[i] = f'{mes_novo} {ano_novo} {quantidade} {tipo_novo}\n'
                    break
                
        with open(FILE_PATH, 'w') as file:
                file.writelines(lines)
        
        return redirect('Prova:informar_rendimento')
    else:
        return redirect('Prova:informar_rendimento')
    
def excluir(request):
    
    if(request.method == 'POST'):
        mes = request.POST.get('mes')
        ano = request.POST.get('ano')
        tipo = request.POST.get('tipo')
    
        with open(FILE_PATH, 'r') as file:
            lines = file.readlines()
        for i in range(len(lines)):
                mes_arquivo, ano_arquivo, quantidade, tipo_arquivo  = lines[i].split()
                if mes == mes_arquivo and ano == ano_arquivo and tipo == tipo_arquivo: 
                    del lines[i]
                    with open(FILE_PATH, 'w') as file:
                        file.writelines(lines)
                    break


