from django.test import TestCase
from model_mommy import mommy
from anuncio.models import Anuncio
from accounts.models import Usuario
from favorito.models import Favorito


class FavoritoTestCase(TestCase):

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

        self.favorito = Favorito.objects.create(
            fk_usuario=self.usuario,
            fk_anuncio=self.anuncio
        )

    def test_str(self):
        self.assertEquals(str(self.favorito), str(self.favorito.id))
