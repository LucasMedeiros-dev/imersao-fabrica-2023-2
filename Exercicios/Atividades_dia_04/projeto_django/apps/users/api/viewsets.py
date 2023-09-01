from rest_framework.viewsets import ModelViewSet
from apps.users.models import Users_app
from .serializers import UserSerializer


class Users_appViewSet(ModelViewSet):

    queryset = Users_app.objects.all()

    serializer_class = UserSerializer
