from django.contrib.auth import get_user_model
from rest_framework import serializers

user_model = get_user_model()


class EmailChangeSerializer(serializers.Serializer):
    current_email = serializers.EmailField(required=True)
    new_email = serializers.EmailField(required=True)
    current_password = serializers.CharField(required=True)

    def validate_new_email(self, value):
        if user_model.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("EMAIL_ALREADY_EXISTS")
        return value
