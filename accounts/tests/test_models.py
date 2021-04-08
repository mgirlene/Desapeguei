from django.test import TestCase
from accounts.models import Usuario

class UsuarioTestCase(TestCase):

    def setUp(self):

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

    def test_str(self):
        self.assertEquals(str(self.usuario), self.usuario.email)
