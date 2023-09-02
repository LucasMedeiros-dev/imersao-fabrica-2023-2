from rest_framework import serializers
from carroceria.models import Carroceria


class CarroceriaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carroceria
        fields = ['id', 'Nome', 'Versao', 'Motor', 'Ano', 'Opcionais']
