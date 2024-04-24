from django.http import HttpResponse
from django.shortcuts import render, redirect
#import PIL
from PIL import Image
import os
from django.conf import settings

#foto = Image.open('/Estudos/Desenvolvimento_de_Software/curso_estacio/Semestre 2/site_de_compras_01/django_ecomerce/src/app/static/images/exclusive.png')

def home(request):
    context = {
        'title': "Página principal",
        'content': "Bem vindo à página inicial"
    } 

    return render(request, 'index.html', context)

def produtos(request):
    return render(request, 'produtos.html')

def contato(request):
    context = {
        'title': "Página de contato",
        'content': "Bem vindo à página de contato"
    }
    return render(request, 'contato.html', context)

def conta(request):
    return render(request, 'conta.html')

def sobre(request):
    return render(request, 'sobre.html')

def formulario(request):
    if request.method == "GET":
        return render(request, "formulario.html")
    elif request.method == "POST":
        file = request.FILES.get("my_file")

        #img = Image.open(file)
        #path = os.path.join(settings.BASE_DIR, f'media/{file.name}')
        #img = img.save(path)
        #print(file)
        return HttpResponse(file)
