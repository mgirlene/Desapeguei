from django.test import TestCase, Client
from model_mommy import mommy
from accounts.models import Usuario
from django.urls import reverse_lazy

class AnuncioViewTestCase(TestCase):

    def setUp(self):
        self.categoria = mommy.make('Categoria')
        self.status = mommy.make('Status')

        self.usuario = Usuario.objects.create(
            email='carla@gmail.com',
            username='carla@gmail.com',
            password='1234@5678',
            first_name='Carla',
            last_name='da silva',
            celular='(88)99999-9999',
            cpf='184.684.200-00',
            data_nascimento='2000-02-11'
        )

        self.dados = {
            'nome': 'Geladeira',
            'preco': 1000,
            'descricao': 'Geladeira semi nova',
            'localizacao' : '63430000',
            'imagem' : '',
            'fk_usuario' : self.usuario,
            'fk_categoria' : self.categoria,
            'fk_status' : self.status
        }

        self.cliente = Client()

    def test_form_create(self):
        request = self.cliente.post(reverse_lazy('anuncio_cadastro'), data=self.dados)
        self.assertEquals(request.status_code, 302)

    def test_list(self):
        dado = {'pk': self.usuario.id}
        request = self.client.get(reverse_lazy('anuncio_lista'), data=dado)
        self.assertEquals(request.status_code, 302)
