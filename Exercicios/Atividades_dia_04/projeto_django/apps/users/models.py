from django.db import models


# Create your models here.


class Users_app(models.Model):
    usuario = models.CharField(max_length=16)
    senha = models.CharField(max_length=24)
    primeiro_nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.primeiro_nome
