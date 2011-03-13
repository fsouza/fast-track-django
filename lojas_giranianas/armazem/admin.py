# -*- coding: utf-8 -*-

from django.contrib import admin
from django.template.defaultfilters import truncatewords
from models import Produto, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('nome', 'mini_descricao', 'preco', 'data_modificacao', 'publicado', 'categoria')
    list_filter = ('publicado', 'categoria',)
    search_fields = ('nome', 'descricao',)
    select_related = True

    def mini_descricao(self, obj):
        return truncatewords(obj.descricao, 10)

    mini_descricao.short_description = 'Descrição'

class CategoriaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('nome', 'supercategoria',)
    list_filter = ('supercategoria',)
    search_fields = ('nome',)
    select_related = True

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria, CategoriaAdmin)
