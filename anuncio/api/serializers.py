from rest_framework import serializers
from ..models import Anuncio

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = ['id', 'nome', 'preco', 'descricao', 'localizacao', 'imagem', 'fk_usuario', 'fk_status', 'fk_categoria']