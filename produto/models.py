from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = 'categoria'
        verbose_name_plural = 'categorias'

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(null=True, blank=True)
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='produtos', null=True, blank=True)
    fk_usuario = models.ForeignKey("accounts.Usuario", on_delete=models.CASCADE)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = 'produto'
        verbose_name_plural = 'produtos'

class ProdutoImagem(models.Model):
    imagem = models.ImageField(upload_to='produtos', null=True, blank=True)
    fk_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        db_table = 'produto_imagem'
        verbose_name_plural = 'produtos_imagens'