from django.contrib.auth import get_user_model
from rest_framework import serializers

UserModel = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'is_staff', 'is_superuser']
        editable_fields = ['email', 'is_staff',  'is_superuser']
