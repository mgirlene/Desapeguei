from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from .forms import AnuncioForm, ContactForm
from .models import Anuncio, Contact
from favorito.models import Favorito
from anuncio.models import Categoria
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
import pycep_correios
from pycep_correios.exceptions import InvalidCEP
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


class AnuncioView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Anuncio
    template_name = 'anuncio/anuncioRegister.html'
    form_class = AnuncioForm
    success_url = 'anuncio_lista'
    success_message = "Anuncio cadastrado com sucesso"

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


class AnuncioUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncio/anuncioUpdate.html'
    success_url = 'anuncio_lista'
    success_message = "Anuncio editado com sucesso"

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class AnuncioDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Anuncio
    template_name = 'anuncio/anuncioDelete.html'
    success_url = 'anuncio_lista'
    success_message = "Anuncio excluido com sucesso"

    def get_success_url(self):
        messages.error(self.request, self.success_message)
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


class ContactForm(SuccessMessageMixin, LoginRequiredMixin, FormView):
    form_class = ContactForm
    template_name = 'anuncio/contact.html'
    success_url = reverse_lazy('index')
    success_message = "Email enviado com sucesso"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_anuncio = self.request.GET.get('anuncio', '')
        anun = Anuncio.objects.get(id=id_anuncio)
        context['email_anuncio'] = anun.fk_usuario.email
        return context

    def form_valid(self, form):
        self.contact = form.save()
        id_anuncio = self.request.GET.get('anuncio', '')
        anuncio = Anuncio.objects.get(id=id_anuncio)
        msg = 'Cliente: ' + self.contact.name + '\n\n' +\
              'Email: ' + self.contact.email + '\n\n' +\
              'Anúncio: ' + anuncio.nome + '\n\n' +\
              'Mensagem: ' + self.contact.mensagem
        send_mail(
            'Interessado em seu produto no Desapeguei',
            '%s' % msg,
            'desapegueidsc@gmail.com',
            [self.contact.destinatario],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())
