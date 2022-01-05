from rest_framework import serializers
from allauth.account.adapter import get_adapter


class PasswordChangeSerializer(serializers.Serializer):
    current_email = serializers.EmailField(required=True)
    current_password = serializers.CharField(required=True)
    new_password1 = serializers.CharField(required=True)
    new_password2 = serializers.CharField(required=True)

    def validate_new_password1(self, password):
        return get_adapter().clean_password(password)

    def validate_new_password2(self, password):
        return get_adapter().clean_password(password)
