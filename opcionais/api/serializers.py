from rest_framework import serializers
from opcionais.models import Opcionais


class OpcionaisSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opcionais
        fields = ['id', 'Nome', 'Equipamentos']
