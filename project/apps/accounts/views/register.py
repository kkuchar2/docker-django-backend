from allauth.account import app_settings as allauth_settings
from allauth.account.utils import complete_signup
from dj_rest_auth.app_settings import JWTSerializer, TokenSerializer, create_token
from dj_rest_auth.models import TokenModel
from dj_rest_auth.registration.app_settings import register_permission_classes, RegisterSerializer
from dj_rest_auth.utils import jwt_encode
from django.conf import settings
from rest_framework import serializers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from rest_framework.decorators import authentication_classes
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.accounts.util import parse_field_errors

'''
        if not user.is_active:
                return JsonResponse({'status': 'error', 'data': 'user_inactive'})

            self.send_email_confirmation(request, user, user.email)

            return JsonResponse({'status': 'success', 'data': 'Confirmation email sent'})
        except Exception as e:
            user.delete()
            raise e

'''
sensitive_post_parameters_m = method_decorator(
    sensitive_post_parameters('password1', 'password2'),
)


@authentication_classes([])
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    token_model = TokenModel
    throttle_scope = 'dj_rest_auth'

    @sensitive_post_parameters_m
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_response_data(self, user):
        if allauth_settings.EMAIL_VERIFICATION == \
                allauth_settings.EmailVerificationMethod.MANDATORY:
            return {'detail': _('Verification e-mail sent.')}

        if getattr(settings, 'REST_USE_JWT', False):
            data = {
                'user': user,
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
            }
            return JWTSerializer(data, context=self.get_serializer_context()).data
        else:
            return TokenSerializer(user.auth_token, context=self.get_serializer_context()).data

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return JsonResponse(parse_field_errors(e))

        self.perform_create(serializer)

        return JsonResponse({'status': 'success', 'data': 'Confirmation email sent'})

    def perform_create(self, serializer):
        user = serializer.save(self.request)

        if allauth_settings.EMAIL_VERIFICATION != allauth_settings.EmailVerificationMethod.MANDATORY:
            if getattr(settings, 'REST_USE_JWT', False):
                self.access_token, self.refresh_token = jwt_encode(user)
            else:
                create_token(self.token_model, user, serializer)

        complete_signup(self.request._request, user, allauth_settings.EMAIL_VERIFICATION, None)

        return user
