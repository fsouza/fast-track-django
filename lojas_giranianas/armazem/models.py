from django.db import models

class ProdutoPublicadoManager(models.Manager):
    def get_query_set(self):
        return super(ProdutoPublicadoManager, self).get_query_set().filter(publicado=True)

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    descricao = models.TextField()
    categoria = models.ForeignKey("Categoria", related_name='produtos')
    preco = models.FloatField()
    publicado = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_modificacao = models.DateTimeField(auto_now=True)

    # Managers
    objects = models.Manager()
    ativos = ProdutoPublicadoManager()

    def __unicode__(self):
        return self.nome

class SuperCategoriaManager(models.Manager):
    def get_query_set(self):
        return super(SuperCategoriaManager, self).get_query_set().filter(supercategoria__isnull=True)

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    supercategoria = models.ForeignKey("Categoria", related_name="subcategorias", blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=100, blank=True)

    # Managers
    objects = models.Manager()
    supercategorias = SuperCategoriaManager()

    def __unicode__(self):
        return self.nome

import signals
