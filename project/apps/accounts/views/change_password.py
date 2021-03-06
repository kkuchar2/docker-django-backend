from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from apps.accounts.serializers import PasswordChangeSerializer
from apps.accounts.util import parse_field_errors, create_form_field_error, create_form_error


class ChangePasswordView(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'dj_rest_auth'

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return JsonResponse(parse_field_errors(e))

        current_email = request.data['current_email']
        password = request.data['current_password']
        new_password1 = request.data['new_password1']
        new_password2 = request.data['new_password2']

        user = authenticate(request=request, email=current_email, password=password)

        if user is None:
            return create_form_field_error("invalid", "current_password", "WRONG_PASSWORD")

        if new_password1 != new_password2:
            return create_form_error("invalid", "PASSWORDS_DO_NOT_MATCH")

        if user.check_password(new_password1):
            return create_form_error("invalid", "SAME_AS_OLD_PASSWORD")

        user.set_password('{}'.format(new_password1))
        user.save()

        return JsonResponse({'status': 'success', 'data': 'Password has been changed'})
