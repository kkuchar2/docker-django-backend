from django.contrib.auth import authenticate, get_user_model
from django.urls import exceptions as url_exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions, serializers

UserModel = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        allow_blank=False,
        error_messages={
            "blank": "EMAIL_REQUIRED",
            "invalid": "INVALID_EMAIL",
            "required": "EMAIL_REQUIRED"
        },
    )
    password = serializers.CharField(
        required=True,
        allow_blank=False,
        error_messages={
            "blank": "PASSWORD_REQUIRED",
            "invalid": "INVALID_PASSWORD",
            "required": "PASSWORD_REQUIRED"
        },
    )

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):
        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_username_email(self, email, password):
        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include either "username" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def get_auth_user_using_allauth(self, email, password):
        return self._validate_email(email, password)

    def get_auth_user(self, email, password):
        try:
            return self.get_auth_user_using_allauth(email, password)
        except url_exceptions.NoReverseMatch:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

    @staticmethod
    def validate_auth_user_status(user):
        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.ValidationError(msg)

    @staticmethod
    def validate_email_verification_status(user):
        email_address = user.emailaddress_set.get(email=user.email)

        if not email_address.verified:
            raise serializers.ValidationError(_('E-mail is not verified.'))

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = self.get_auth_user(email, password)

        if not user:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # Did we get back an active user?
        self.validate_auth_user_status(user)

        # Validate is user has confirmed email address
        self.validate_email_verification_status(user)

        attrs['user'] = user

        return attrs
