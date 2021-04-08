from django.test import TestCase
from model_mommy import mommy
from anuncio.models import Anuncio
from accounts.models import Usuario


class AnuncioTestCase(TestCase):

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

        self.anuncio = Anuncio.objects.create(
            nome='Cadeira',
            preco=1000,
            descricao='Cadeira gamer nova',
            localizacao='59920000',
            imagem=None,
            fk_usuario=self.usuario,
            fk_categoria=self.categoria,
            fk_status=self.status
        )

    def test_str(self):
        self.assertEquals(str(self.anuncio), self.anuncio.nome)


class CategoriaTestCase(TestCase):

    def setUp(self):
        self.categoria = mommy.make('Categoria')

    def test_str(self):
        self.assertEquals(str(self.categoria), self.categoria.nome)


class StatusTestCase(TestCase):

    def setUp(self):
        self.status = mommy.make('Status')

    def test_str(self):
        self.assertEquals(str(self.status), self.status.nome)
