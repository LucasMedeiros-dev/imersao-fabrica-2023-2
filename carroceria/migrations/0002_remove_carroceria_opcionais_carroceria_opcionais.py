# Generated by Django 4.2.4 on 2023-09-02 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcionais', '0001_initial'),
        ('carroceria', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carroceria',
            name='Opcionais',
        ),
        migrations.AddField(
            model_name='carroceria',
            name='opcionais',
            field=models.ManyToManyField(to='opcionais.opcionais'),
        ),
    ]
