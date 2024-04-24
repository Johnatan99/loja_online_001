from django.shortcuts import render, redirect
#from django.conf import settings
#import django 
# Create your views here.
 
#if not settings.configured:
 #   settings.configure()
#django.setup()
from models import Product


def produtos(request):
    context = {
        'title': "Página de produtos",
        'content': "Bem vindo à página de produtos"
    }
    return render(request, 'produtos.html', context)

    id = 1
#def delete(request, id):
 #   produto = Product.objects.get(id_produto=id)
  #  produto.delete()
   # return redirect('/')

#delete(id)