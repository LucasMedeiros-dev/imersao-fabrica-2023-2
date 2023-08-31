from django.urls import path,include
from rest_framework import routers

from apps.todo.api.viewsets import TaskViewSet

router = routers.DefaultRouter()
router.register('', TaskViewSet, basename='Task')

urlpatterns = [
    path('',include(router.urls)),
]
