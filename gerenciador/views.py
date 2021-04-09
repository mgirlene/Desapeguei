from django.views.generic import ListView
from anuncio.models import Anuncio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from favorito.models import Favorito


class Index(ListView):
    model = Anuncio
    context_object_name = 'anuncio_list'
    template_name = 'gerenciador/index.html'

    def get_queryset(self):
        id_user = self.request.user.id

        anuncio = ""

        search = self.request.GET.get('search', '')
        if search:
            anuncio = Anuncio.objects.filter(Q(nome__icontains=search))

        if not anuncio:
            anuncio = Anuncio.objects.all()

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

        context['favoritos'] = list
        return context
