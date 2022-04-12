from django.contrib.auth import get_user_model
from rest_framework import viewsets

from apps.accounts.serializers import CustomUserDetailSerializer

UserModel = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = CustomUserDetailSerializer
