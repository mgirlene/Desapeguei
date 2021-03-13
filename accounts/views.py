from django.views.generic.edit import CreateView, UpdateView
from .models import Usuario
from .forms import UsuarioRegisterForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class UserCreate(CreateView):
    model = Usuario
    template_name = 'accounts/register.html'
    form_class = UsuarioRegisterForm
    success_url = 'login'

    def form_valid(self, form):
        self.usuario = form.save()

        send_mail(
            'Cliente Cadastrado',
            '%s, Você foi cadastrado com sucesso!' % self.usuario.first_name,
            'desapegueidsc@gmail.com',
            [self.usuario.email],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        messages.success(self.request, 'Usuário cadastrado com sucesso!')
        return reverse_lazy(self.success_url)


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = Usuario
    fields = ('first_name', 'last_name', 'cpf', 'data_nascimento', 'celular')
    template_name = 'accounts/update_user.html'
    success_url = reverse_lazy('index')
