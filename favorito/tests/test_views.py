from django.test import TestCase, Client
from model_mommy import mommy
from accounts.models import Usuario
from anuncio.models import Anuncio
from django.urls import reverse_lazy

class AnuncioViewTestCase(TestCase):

    def setUp(self):

        self.usuario = {
            'email': 'carla@gmail.com',
            'username': 'carla@gmail.com',
            'password1': '1234@5678',
            'password2': '1234@5678',
            'first_name': 'Carla',
            'last_name': 'da silva',
            'celular': '(88)99999-9999',
            'cpf': '184.684.200-00',
            'data_nascimento': '2000-02-11'
        }

        self.categoria = {
            'nome' : 'Imoveis'
        }

        self.status = {
            'nome': 'Vendido'
        }

        self.anuncio = {
            'nome': 'Geladeira',
            'preco': 1000,
            'descricao': 'Geladeira semi nova',
            'localizacao': '63430000',
            'imagem': '',
            'fk_usuario': self.usuario,
            'fk_categoria': self.categoria,
            'fk_status': self.status
        }

        self.dados = {
            'fk_usuario' : self.usuario,
            'fk_anuncio' : self.anuncio
        }

        self.cliente = Client()

    def test_form_create(self):
        request = self.cliente.post(reverse_lazy('add_favorito'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_list(self):
        request = self.client.get(reverse_lazy('list_favorito'))
        self.assertEquals(request.status_code, 302)