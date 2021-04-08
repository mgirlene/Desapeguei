from rest_framework import viewsets
from ..models import Usuario
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    '''API de Usuário'''
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer