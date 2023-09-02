from django.db import models

# Create your models here.


class Motor(models.Model):
    '''### Modelo dos Motores na DB.\n
    \n
    Contém\n
    `Nome`: CharField com no máx 50 caracteres.\n
    `Litragem`: DecimalField com no maximo 4 digitos e 1 casa após a vírgula
    '''
    Nome = models.CharField(max_length=50)
    Litragem = models.DecimalField(decimal_places=1, max_digits=4)
    Turbo = models.BooleanField()

    def __str__(self) -> str:
        return self.Nome
