from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Usuario
from .forms import UsuarioRegisterForm
from django.urls import reverse_lazy

class UserCreate(CreateView):
    model = Usuario
    template_name = 'accounts/register.html'
    form_class = UsuarioRegisterForm
    success_url = reverse_lazy('login')
