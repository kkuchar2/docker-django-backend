from dj_rest_auth.app_settings import PasswordResetSerializer
from django.http import JsonResponse
from rest_framework.decorators import authentication_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework import serializers

from apps.accounts.util import parse_field_errors


@authentication_classes([])
class ForgotPasswordView(GenericAPIView):
    """
    Calls Django Auth PasswordResetForm save method.

    Accepts the following POST parameters: email
    Returns the success/fail message.
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)
    throttle_scope = 'dj_rest_auth'

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return JsonResponse(parse_field_errors(e))

        serializer.save()

        return JsonResponse({'status': 'success', 'data': 'Reset password link sent'})
