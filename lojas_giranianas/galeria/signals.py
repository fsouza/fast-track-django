from django.db.models.signals import pre_save
from django.dispatch import receiver
from galeria.models import Imagem
from util import gerar_slug

@receiver(pre_save, sender=Imagem)
def gerar_slug_imagem(sender, **kwargs):
    gerar_slug(sender, kwargs['instance'], 'legenda')
