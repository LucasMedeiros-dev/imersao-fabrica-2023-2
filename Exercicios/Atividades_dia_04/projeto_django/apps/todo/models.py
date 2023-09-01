from django.db import models

from apps.users.models import User
# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    date = models.DateField()

    user = models.ForeignKey( User, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.name
