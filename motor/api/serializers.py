from rest_framework import serializers
from motor.models import Motor


class MotorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Motor
        fields = ['id', 'Nome', 'Litragem', 'Turbo']
