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
        if id_user:
            anuncio = Anuncio.objects.filter(~Q(fk_usuario=id_user))
        else:
            anuncio = Anuncio.objects.all()
        return anuncio
