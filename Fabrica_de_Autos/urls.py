from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('carroceria/', include("carroceria.urls")),
    path('motor/', include("motor.urls")),
    path('opcionais/', include("opcionais.urls")),
]
