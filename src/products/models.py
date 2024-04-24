from django.db import models

#from django.conf import settings
#import django 

# Create your models here.

#if not settings.configured:
#    settings.configure()
#django.setup() 

class Product(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=120, null=True)
    foto_produto = models.ImageField(upload_to="products/", null = True, blank= True)
    nota = models.IntegerField(null=True)
    valor = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    categoria = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.nome_produto

    