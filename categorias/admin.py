from django.contrib import admin

#para importar o models Categoria
from .models import Categoria

#nome_cat (nome da categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cat')
    list_display_links = ('id', 'nome_cat')

    #registrar o Categoria

admin.site.register (Categoria, CategoriaAdmin)


