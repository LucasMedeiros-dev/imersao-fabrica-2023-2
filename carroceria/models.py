from django.db import models
from motor.models import Motor
from opcionais.models import Opcionais
# Create your models here.


class Carroceria(models.Model):
    '''### Modelo das Carrocerias na DB.\n
    \n
    Contém\n
    `Nome`: CharField com no máx 50 caracteres.\n
    `Versao`: CharField com no máx 70 caracteres.\n
    `Motor`: Recebe a classe Motor de motor.models.\n
    `Ano`: IntegerField, recebe apenas inteiros\n
    `Opcionais`: ManyToMany que permite a selecao de vários ao mesmo tempo.
    '''
    Nome = models.CharField(max_length=70)
    Versao = models.CharField(max_length=70)
    Motor = models.ForeignKey(Motor, on_delete=models.CASCADE, null=False)
    Ano = models.IntegerField()
    Opcionais = models.ManyToManyField(Opcionais)

    def __str__(self) -> str:
        return self.Nome
