from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'is_staff', 'is_active')
        read_only_fields = ('email',)
