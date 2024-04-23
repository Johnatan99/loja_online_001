from django.db import models

# Create your models here.

class Product(models.Model):
    #id_produto =
    nome_produto = models.Charfield(max_length=120)
    #foto_produto
    #nota =
    valor = models.DecimalField(decimal_places=2, max_digts=20, default=100.00)
    #categoria
    descricao = models.TextField()
    