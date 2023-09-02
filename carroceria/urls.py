from django.urls import path, include
from rest_framework import routers

from carroceria.api.viewsets import CarroceriaViewSet

router = routers.DefaultRouter()  # Instancia a classe router que define as URLS
# Registra o ViewSet da classe
router.register('', CarroceriaViewSet, basename='carroceria')

urlpatterns = [
    path('', include(router.urls)),
]
