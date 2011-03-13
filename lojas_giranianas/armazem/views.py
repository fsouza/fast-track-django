# Create your views here.
from django.views.generic.list import ListView
from models import Categoria, Produto

class ProdutosPorCategoriaListView(ListView):
    context_object_name = 'produtos'
    template_name = 'armazem/produtos_por_categoria_list.html'

    def get_queryset(self):
        return Produto.objects.select_related().filter(categoria__slug=self.kwargs['slug_categoria'])

    def get_context_data(self, **kwargs):
        context = super(ProdutosPorCategoriaListView, self).get_context_data(**kwargs)
        context['categoria'] = Categoria.objects.get(slug=self.kwargs['slug_categoria'])
        return context
