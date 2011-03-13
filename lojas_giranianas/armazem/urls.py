from django.conf.urls.defaults import *
from armazem.views import CategoriaDetailView, ProdutosPorCategoriaListView
from models import Produto, Categoria

urlpatterns = patterns('',
    url(r'^produto/(?P<slug>[\w-]+)$', 'django.views.generic.list_detail.object_detail', { 'queryset' : Produto.ativos.all(), 'template_object_name' : 'produto' }, name='ver_produto'),
    url(r'^produtos/(?P<slug_categoria>[\w-]+)$', ProdutosPorCategoriaListView.as_view(paginate_by=10), name='listar_produtos_por_categoria'),
    url(r'^produtos', 'django.views.generic.list_detail.object_list', { 'queryset' : Produto.ativos.all(), 'paginate_by' : 10 }, name='listar_produtos'),
    url(r'^categorias/(?P<slug>[\w-]+)$', 'django.views.generic.list_detail.object_detail', { 'template_object_name' : 'categoria', 'queryset' : Categoria.objects.select_related() }, name='ver_categoria'),
    url(r'^categorias/', 'django.views.generic.list_detail.object_list', { 'queryset' : Categoria.supercategorias.all() }, name='listar_categorias'),
)
