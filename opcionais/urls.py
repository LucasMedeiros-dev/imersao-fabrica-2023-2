from django.urls import path, include
from rest_framework import routers

from opcionais.api.viewsets import OpcionaisViewSet

router = routers.DefaultRouter()  # Instancia a classe router que define as URLS
# Registra o ViewSet da classe
router.register('', OpcionaisViewSet, basename='opcionais')

urlpatterns = [
    path('', include(router.urls)),
]
