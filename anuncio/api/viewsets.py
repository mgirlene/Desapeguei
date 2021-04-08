from rest_framework import viewsets
from ..models import Anuncio
from .serializers import AnuncioSerializer

class AnuncioViewSet(viewsets.ModelViewSet):
    '''API Anúncio'''
    queryset = Anuncio.objects.all()
    serializer_class = AnuncioSerializer