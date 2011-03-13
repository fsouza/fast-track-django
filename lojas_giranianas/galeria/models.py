from django.db import models

# Create your models here.
class Imagem(models.Model):
    legenda = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True)
    produto = models.ForeignKey("armazem.Produto", related_name='fotos', on_delete=models.CASCADE)
    original = models.ImageField(upload_to="uploads/galeria/original", max_length=100, blank=True)
    thumb = models.ImageField(upload_to="uploads/galeria/thumb", max_length=100, blank=True)
    principal = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "imagens"

    def __unicode__(self):
        return self.legenda

import signals
