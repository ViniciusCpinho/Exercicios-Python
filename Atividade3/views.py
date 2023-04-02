import os
from django.shortcuts import render, redirect
from .models import File

APP_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(APP_DIR, 'Files')
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)
FILE_PATH = os.path.join(BASE_DIR, 'ArquivoNotas.txt')

erro = 'Não há arquivos registrados'

def get_arquivo(request):
        
    try:
        if os.path.getsize(FILE_PATH) == 0:
            return render(request, 'Atividade3_Index.html', {'files': erro})
        else:
            files = open(FILE_PATH, 'r')
            files_line = files.readlines()
            
            data = []
            for aluno in files_line:
                nome, nota_um, nota_dois, nota_tres = aluno.split()
                data.append({
                    'nome': nome,
                    'nota_um': nota_um,
                    'nota_dois': nota_dois,
                    'nota_tres': nota_tres,
                })
            return render(request, 'Atividade3_Index.html', {'files':data})
    except FileNotFoundError:
        return render(request, 'Atividade3_Index.html', {'files': erro})

def post_arquivo(request):
    
    if(request.method == 'POST'):
        nome = request.POST.get('nome', '')
        nota_um = request.POST.get('nota_um', '')
        nota_dois = request.POST.get('nota_dois', '')
        nota_tres = request.POST.get('nota_tres', '')
        
        data = f'{nome} {nota_um} {nota_dois} {nota_tres}\n'
        
        with open(FILE_PATH, '+a') as file:
            file.write(data)
        
        return redirect('Atividade3:get_arquivo')
    else:
        return redirect('Atividade3_Index.html')
