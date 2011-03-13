from django.db.models.signals import pre_save
from django.dispatch import receiver
from armazem.models import Produto, Categoria
from util import gerar_slug

@receiver(pre_save, sender=Produto)
def gerar_slug_produto(sender, **kwargs):
    gerar_slug(sender, kwargs['instance'])

@receiver(pre_save, sender=Categoria)
def gerar_slug_categoria(sender, **kwargs):
    gerar_slug(sender, kwargs['instance'])
