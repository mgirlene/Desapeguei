from django.test import TestCase
from .models import Usuario

class usuarioTest(TestCase):
    def setUp(self):
        Usuario.objects.create(
            email='teste@gmail.com',
            username='teste@gmail.com',
            password='1234@5678',
            first_name='teste',
            last_name='da silva',
            celular='(88)99999-9999',
            cpf='184.684.200-00',
            data_nascimento='2000-02-11'

        )

    def teste1(self):
        user = Usuario.objects.get(email='teste@gmail.com')
        self.assertEquals(user.email, 'teste@gmail.com')

    def teste2(self):
        user = Usuario.objects.get(email='teste@gmail.com', password='1234@5678')
        self.assertEquals(user.email, 'teste@gmail.com')

    def teste3(self):
        user = Usuario.objects.get(email='teste@gmail.com', password='1234@567')
        self.assertEquals(user.email, 'teste@gmail.com')