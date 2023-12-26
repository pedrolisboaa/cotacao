from django.db import models

# Create your models here.
class Moeda(models.Model):
    sigla = models.CharField(("Sigla"), max_length=3)
    moeda = models.CharField(('Moeda'), max_length=50)
    bandeira = models.ImageField(upload_to='bandeiras')

    class Meta:
        verbose_name = 'Moeda'
        verbose_name_plural = 'Moedas'

    def __str__(self):
        return self.moeda
