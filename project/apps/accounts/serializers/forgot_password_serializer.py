from rest_framework import serializers

from apps.accounts.forms import PasswordResetForm
from settings import settings

if 'allauth' in settings.INSTALLED_APPS:
    from allauth.account.forms import default_token_generator
else:
    from django.contrib.auth.tokens import default_token_generator


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password_reset_form_class = PasswordResetForm

    def get_email_options(self):
        """Override this method to change default e-mail options"""
        return {}

    def validate_email(self, value):
        # Create PasswordResetForm with the serializer
        self.reset_form = self.password_reset_form_class(data=self.initial_data)
        if not self.reset_form.is_valid():
            raise serializers.ValidationError(self.reset_form.errors)

        return value

    def save(self):
        request = self.context.get('request')
        # Set some values to trigger the send_email method.
        opts = {
            'use_https': request.is_secure(),
            'from_email': getattr(settings, 'DEFAULT_FROM_EMAIL'),
            'request': request,
            'token_generator': default_token_generator
        }

        opts.update(self.get_email_options())
        self.reset_form.save(**opts)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
