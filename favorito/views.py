from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Favorito
from anuncio.models import Anuncio
from .form import FavoritoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required


class FavoritoView(LoginRequiredMixin, CreateView):
    model = Favorito
    fields = ['fk_usuario', 'fk_anuncio']
    template_name = "gerenciador/index.html"

    def post(self, request, *args, **kwargs):

        form = FavoritoForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('fk_usuario')
            anuncio = form.cleaned_data.get('fk_anuncio')

            fav = Favorito.objects.filter(fk_usuario=usuario, fk_anuncio=anuncio).exists()

            if fav:
                messages.warning(request, 'Esse anúncio já foi favoritado')

            else:
                favorit = form.save()
                favorit.save()
                messages.success(request, 'Anúncio adicionado aos favoritos')

        return redirect('index')

@login_required
def deleteFavoritas(request, pk):
    usuario = request.user
    anuncio = Favorito.objects.get(fk_anuncio=pk, fk_usuario=usuario.id)
    anuncio.delete()
    messages.error(request, 'Anúncio removido dos favoritos')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def listFavoritas(request):
    data = {}

    anuncios = Anuncio.objects.all()
    usuario = request.user
    favoritos = Favorito.objects.filter(fk_usuario=usuario.id)
    list = []
    for i in range(0, len(favoritos)):
        fav = favoritos[i]
        list += anuncios.filter(id=fav.fk_anuncio_id)[0:1]

    data['anuncios'] = list

    return render(request, 'favorito/anuncio_favoritos.html', data)
