from django.http import HttpResponse
from django.shortcuts import render, redirect

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
# Create your views here.
