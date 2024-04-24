from django.shortcuts import render
from django.conf import settings
settings.configure()
from models import Product
# Create your views here.

def produtos(request):
    context = {
        'title': "Página de produtos",
        'content': "Bem vindo à página de produtos"
    }
    return render(request, 'produtos.html', context)
