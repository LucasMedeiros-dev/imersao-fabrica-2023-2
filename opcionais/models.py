from django.db import models

# Create your models here.


class Opcionais(models.Model):
    '''### Modelo dos Opcionais na DB.\n
    \n
    Contém\n
    `Nome`: CharField com no máx 50 caracteres.\n
    `Equipamentos`: TextField
    '''
    Nome = models.CharField(max_length=50)
    Equipamentos = models.TextField()

    def __str__(self) -> str:
        return self.Nome
