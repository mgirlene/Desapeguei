from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

class Login(TemplateView):
    template_name = 'accounts/login.html'

class Register(TemplateView):
    template_name = 'accounts/register.html'

class Password(TemplateView):
    template_name = 'accounts/password.html'