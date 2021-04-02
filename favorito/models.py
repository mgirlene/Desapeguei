from django.db import models

class Favorito(models.Model):
    fk_usuario = models.ForeignKey("accounts.Usuario", on_delete=models.CASCADE)
    fk_anuncio = models.ForeignKey("anuncio.Anuncio", on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        db_table = 'favorito'
        verbose_name_plural = 'favoritos'