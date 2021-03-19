from django.views.generic import ListView
from produto.models import Produto
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class Index(ListView):
    model = Produto
    context_object_name = 'produto_list'
    template_name = 'gerenciador/index.html'

    def get_queryset(self):
        print("njbghjebhgbejghberjhgb")
        id_user = self.request.user.id
        if id_user:
            produtos = Produto.objects.filter(~Q(fk_usuario=id_user))
        else:
            produtos = Produto.objects.all()
        print("88855555555665555")
        print(produtos)
        return produtos
