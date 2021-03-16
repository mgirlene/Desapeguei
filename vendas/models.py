from django.db import models

class Vendas(models.Model):
    data = models.DateField()
    fk_cliente = models.ForeignKey("accounts.Usuario", on_delete=models.CASCADE)
    fk_produtos = models.ManyToManyField("produto.Produto", related_name="vendas_produto")

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        db_table = 'vendas'
        verbose_name_plural = 'vendas'