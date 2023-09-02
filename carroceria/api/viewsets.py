from rest_framework.viewsets import ModelViewSet
from carroceria.models import Carroceria
from carroceria.api.serializers import CarroceriaSerializers
from carroceria.api.paginacao import PaginacaoPadrao


class CarroceriaViewSet(ModelViewSet):

    queryset = Carroceria.objects.all()
    serializer_class = CarroceriaSerializers
    pagination_class = PaginacaoPadrao
