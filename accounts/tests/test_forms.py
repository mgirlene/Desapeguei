from django.test import TestCase
from accounts.forms import UsuarioRegisterForm

class UsuarioRegisterFormTestCase(TestCase):

    def setUp(self):
        self.email = 'carla@gmail.com'
        self.username = 'carla@gmail.com'
        self.password1 = '1234@5678'
        self.password2 = '1234@5678'
        self.first_name = 'Carla'
        self.last_name = 'da silva'
        self.celular = '(88)99999-9999'
        self.cpf = '184.684.200-00'
        self.data_nascimento = '2000-02-11'

        self.dados = {
            'email' : self.email,
            'username' : self.username,
            'password1' : self.password1,
            'password2' : self.password2,
            'first_name' : self.first_name,
            'last_name' : self.last_name,
            'celular' : self.celular,
            'cpf' : self.cpf,
            'data_nascimento' : self.data_nascimento
        }

        self.form = UsuarioRegisterForm(data=self.dados)


    def test_save(self):

        self.assertTrue(self.form.save())
