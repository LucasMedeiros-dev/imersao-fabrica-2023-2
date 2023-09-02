from django.urls import path, include
from rest_framework import routers

from motor.api.viewsets import MotorViewSet

router = routers.DefaultRouter()  # Instancia a classe router que define as URLS
# Registra o ViewSet da classe
router.register('', MotorViewSet, basename='motor')

urlpatterns = [
    path('', include(router.urls)),
]
