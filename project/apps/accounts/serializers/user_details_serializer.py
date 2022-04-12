from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers

from .user_profile_serializer import UserProfileSerializer
from .email_address_serializer import EmailAddressSerializer


class CustomUserDetailSerializer(UserDetailsSerializer):
    profile = UserProfileSerializer(source="userprofile")
    email = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ('profile', 'email')

    def get_email(self, user):
        email_address = EmailAddress.objects.filter(email=user.email)[0]
        serializer = EmailAddressSerializer(instance=email_address)
        return serializer.data
