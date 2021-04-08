from rest_framework import serializers
from ..models import Usuario

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'data_nascimento', 'celular', 'cpf']