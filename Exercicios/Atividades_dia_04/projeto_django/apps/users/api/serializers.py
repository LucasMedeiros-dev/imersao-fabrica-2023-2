from rest_framework import serializers
from apps.users.models import Users_app


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_app
        fields = ['id', 'usuario', 'senha',
                  'primeiro_nome', 'sobrenome', 'email']
