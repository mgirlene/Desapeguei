from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = 'categoria'
        verbose_name_plural = 'categorias'

class Status(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = 'status'
        verbose_name_plural = 'status'

class Anuncio(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True, blank=True)
    localizacao = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='anuncios', null=True, blank=True)
    fk_usuario = models.ForeignKey("accounts.Usuario", on_delete=models.CASCADE)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fk_status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = 'anuncio'
        verbose_name_plural = 'anuncios'
