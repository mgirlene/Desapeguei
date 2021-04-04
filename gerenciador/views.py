from django.views.generic import ListView
from anuncio.models import Anuncio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


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

        return anuncio
