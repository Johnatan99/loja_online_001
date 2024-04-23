from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    #foto_produto
    valor = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    nota = models.IntegerField()
    categoria = models.CharField(max_length=50, default="Sem categoria")
    