from django.views.generic import ListView
from anuncio.models import Anuncio
from django.db.models import Q
from favorito.models import Favorito
from anuncio.models import Categoria
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class Index(SuccessMessageMixin, ListView):
    model = Anuncio
    context_object_name = 'anuncio_list'
    template_name = 'gerenciador/index.html'

    def get_queryset(self):
        id_user = self.request.user.id

        anuncio = ""

        search = self.request.GET.get('search', '')
        categ = self.request.GET.get('cat', '')

        if search:
            anuncio = Anuncio.objects.filter(Q(nome__icontains=search))

        if categ:
            anuncio = Anuncio.objects.filter(Q(fk_categoria=categ), ~Q(fk_usuario=id_user))

        if not anuncio:
            anuncio = Anuncio.objects.all()
            if search or categ:
                messages.error(self.request, "Nenhum anúncio existente na sua consulta")

        if id_user:
            anuncio = anuncio.filter(~Q(fk_usuario=id_user))

            if not anuncio:
                anuncio = Anuncio.objects.filter(~Q(fk_usuario=id_user))

        anuncio = anuncio.filter(fk_status=1)

        return anuncio

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        favoritos = Favorito.objects.filter(fk_usuario=user.id)
        list = []
        for i in range(0, len(favoritos)):
            fav = favoritos[i]
            list.append(fav.fk_anuncio_id)

        context['TipoCategoria'] = Categoria.objects.all()
        context['favoritos'] = list
        return context
