from rest_framework import viewsets
from ..models import Favorito
from .serializers import FavoritoSerializer

class AnuncioViewSet(viewsets.ModelViewSet):
    '''API Favoritos'''
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer