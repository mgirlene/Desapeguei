from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView, DetailView
from .forms import AnuncioForm
from .models import Anuncio
from favorito.models import Favorito
from anuncio.models import Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
import pycep_correios
from pycep_correios.exceptions import InvalidCEP


class AnuncioView(LoginRequiredMixin, CreateView):
    model = Anuncio
    template_name = 'anuncio/anuncioRegister.html'
    form_class = AnuncioForm
    success_url = 'anuncio_lista'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['TipoCategoria'] = Categoria.objects.all()
        return context

    def form_valid(self, form):
        anuncio = form.save(commit=False)
        anuncio.fk_usuario = self.request.user
        anuncio.save()
        return super(AnuncioView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class AnuncioUpdateView(LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncio/anuncioUpdate.html'
    success_url = 'anuncio_lista'

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class AnuncioDeleteView(LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/anuncioDelete.html'
    success_url = 'anuncio_lista'

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class AnuncioListView(LoginRequiredMixin, ListView):
    model = Anuncio
    context_object_name = 'anuncio_list'
    template_name = 'anuncio/anuncioList.html'

    def get_queryset(self):
        id_user = self.request.user.id
        anuncio = Anuncio.objects.filter(fk_usuario=id_user)

        return anuncio

class AnuncioDetailsView(DetailView):
    model = Anuncio
    template_name = 'anuncio/anuncioDetails.html'

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Anuncio, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        anuncio = self.kwargs.get("pk")
        user = self.request.user
        favoritos = Favorito.objects.filter(fk_usuario=user.id, fk_anuncio=anuncio)
        list = []
        for i in range(0, len(favoritos)):
            fav = favoritos[i]
            list.append(fav.fk_anuncio_id)

        anunc = Anuncio.objects.get(id=anuncio)
        try:
            endereco = pycep_correios.get_address_from_cep(anunc.localizacao)
        except InvalidCEP:
            endereco['cidade'] = 'None'
            endereco['uf'] = 'None'
            endereco['cep'] = 'None'

        context['favoritos'] = list
        context['endereco_cep'] = endereco['cep']
        context['endereco_cid'] = endereco['cidade']
        context['endereco_uf'] = endereco['uf']
        return context