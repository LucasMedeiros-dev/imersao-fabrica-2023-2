from django.urls import path, include
from rest_framework import routers

from apps.users.api.viewsets import Users_appViewSet

router = routers.DefaultRouter()
router.register('', Users_appViewSet, basename='Users')

urlpatterns = [
    path('', include(router.urls)),
]
