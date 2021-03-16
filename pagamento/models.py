from django.db import models


class Status(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nome)

    class Meta:
        db_table = 'status'
        verbose_name_plural = 'status'


class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    fk_status = models.ForeignKey(Status, on_delete=models.CASCADE)
    fk_usuario = models.ForeignKey("accounts.Usuario", on_delete=models.CASCADE)
    fk_carrinho = models.ForeignKey("carrinho.Carrinho", on_delete=models.CASCADE)