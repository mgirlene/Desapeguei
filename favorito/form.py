from django.forms import ModelForm
from .models import Favorito


class FavoritoForm(ModelForm):
    class Meta:
        model = Favorito
        fields = ['fk_usuario', 'fk_anuncio']