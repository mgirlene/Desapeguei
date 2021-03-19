from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import ProdutoForm
from .models import Produto
from produto.models import Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class ProdutoView(LoginRequiredMixin, CreateView):
    model = Produto
    template_name = 'produto/cadastroProduto.html'
    form_class = ProdutoForm
    success_url = 'index'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TipoCategoria'] = Categoria.objects.all()
        return context

    def form_valid(self, form):
        produto = form.save(commit=False)
        produto.fk_usuario = self.request.user
        produto.save()
        return super(ProdutoView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class ProdutoUpdateView(LoginRequiredMixin, UpdateView):
    model = Produto
    form_class = ProdutoForm
    template_name = 'produto/produtoUpdate.html'
    success_url = 'index'

    def get_success_url(self):
        return reverse_lazy(self.success_url)

class ProdutoDeleteView(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'produto/produtoDelete.html'
    success_url = 'index'

    def get_success_url(self):
        return reverse_lazy(self.success_url)

class ProdutoListView(LoginRequiredMixin, ListView):
    model = Produto
    context_object_name = 'produto_list'
    template_name = 'produto/produtoList.html'

    def get_queryset(self):
        id_user = self.request.user.id
        produtos = Produto.objects.filter(fk_usuario=id_user)
        print(produtos)
        return produtos
