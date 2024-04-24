from django.db import models

# Create your models here.


class Product(models.Model):
    nome_produto = models.CharField(max_length=120, null=True)
    foto_produto = models.ImageField(upload_to="products/", null = True, blank= True)
    nota = models.IntegerField(null=True)
    valor = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)
    categoria = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "produto"

    def __str__(self):
        return self.nome_produto