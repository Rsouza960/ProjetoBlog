from django.db import models


#nome_cat (nome da categoria)
class Categoria(models.Model):
    nome_cat = models.CharField(max_length=50)
