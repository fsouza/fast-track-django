from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<slug_produto>[\w-]+)/(?P<slug>[\w-]+)$', 'galeria.views.ver_foto',  name="ver_foto"),
    url(r'^(?P<slug>[\w-]+)$', 'galeria.views.fotos_produto', name='fotos_produto'),
)
