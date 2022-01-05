from rest_framework import serializers


class EmailChangeSerializer(serializers.Serializer):
    current_email = serializers.EmailField(required=True)
    new_email = serializers.EmailField(required=True)
    current_password = serializers.CharField(required=True)
