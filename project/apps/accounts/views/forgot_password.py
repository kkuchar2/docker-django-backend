from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import authentication_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

from apps.accounts.serializers import ForgotPasswordSerializer
from apps.accounts.util import parse_field_errors


@authentication_classes([])
class ForgotPasswordView(GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    permission_classes = (AllowAny,)
    throttle_scope = 'dj_rest_auth'

    def post(self, request, *args, **kwargs):
        # TODO: Fix issue, when account is inactive and we try to reset password through forgot password link
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return JsonResponse(parse_field_errors(e))

        serializer.save()

        return JsonResponse({'status': 'success', 'data': 'Reset password link sent'})
