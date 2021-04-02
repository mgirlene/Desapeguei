from django.forms import ModelForm
from .models import Anuncio

class AnuncioForm(ModelForm):
    class Meta:
        model = Anuncio
        fields = ('nome', 'preco', 'descricao', 'localizacao', 'imagem', 'fk_categoria', 'fk_usuario', 'fk_status')