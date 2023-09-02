from rest_framework.viewsets import ModelViewSet
from opcionais.models import Opcionais
from opcionais.api.serializers import OpcionaisSerializers
from opcionais.api.paginacao import PaginacaoPadrao


class OpcionaisViewSet(ModelViewSet):

    queryset = Opcionais.objects.all()
    serializer_class = OpcionaisSerializers
    pagination_class = PaginacaoPadrao
