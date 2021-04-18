from django.forms import ModelForm
from .models import Anuncio, Contact

class AnuncioForm(ModelForm):
    class Meta:
        model = Anuncio
        fields = ('nome', 'preco', 'descricao', 'localizacao', 'imagem', 'fk_categoria', 'fk_usuario', 'fk_status')

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'destinatario', 'mensagem')
