from rest_framework.viewsets import ModelViewSet
from motor.models import Motor
from motor.api.serializers import MotorSerializers
from motor.api.paginacao import PaginacaoPadrao


class MotorViewSet(ModelViewSet):

    queryset = Motor.objects.all()
    serializer_class = MotorSerializers
    pagination_class = PaginacaoPadrao
