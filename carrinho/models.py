from django.db import models

class Carrinho(models.Model):
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    fk_usuario = models.ForeignKey("accounts.Usuario", on_delete=models.CASCADE)
    fk_produtos = models.ManyToManyField("produto.Produto", related_name="carrinho_produto")

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        db_table = 'carrinho'
        verbose_name_plural = 'carrinhos'