# Create your views here.
from django.views.generic.list_detail import object_detail
from armazem.models import Produto
from galeria.models import Imagem

def fotos_produto(request, slug):
    return object_detail(request, queryset=Produto.objects.select_related('fotos'), template_object_name='produto', slug=slug, template_name='galeria/fotos_produto.html')

def ver_foto(request, slug_produto, slug):
    return object_detail(request, queryset=Imagem.objects.select_related('produto'), template_object_name='imagem', slug=slug)
