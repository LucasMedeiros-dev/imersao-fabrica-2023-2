from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda/', include("apps.todo.urls")),
    path('usuarios/', include("apps.users.urls"))
]
