import Image

from django.contrib import admin
from galeria.models import Imagem

class ImagemAdmin(admin.ModelAdmin):
    exclude = ('thumb', 'slug', )
    list_display = ('legenda', 'principal', 'produto',)
    search_fields = ('produto__nome',)
    select_related = True

    def save_model(self, request, obj, form, change):
        imagem = form.save()

        nome = imagem.original.name.split('/')[-1]
        imagem.thumb = 'uploads/galeria/thumb/%s' % nome

        original = Image.open(imagem.original.path)
        original.thumbnail((600, 600), Image.ANTIALIAS)
        original.save(imagem.original.path)

        thumbnail = Image.open(imagem.original.path)
        thumbnail.thumbnail((150, 150), Image.ANTIALIAS)
        thumbnail.save(imagem.thumb.path)

        imagem.save()

admin.site.register(Imagem, ImagemAdmin)
