from django.contrib.auth import authenticate, get_user_model
from django.http import JsonResponse
from rest_framework import serializers, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from allauth.account.models import EmailAddress
from apps.accounts.serializers import EmailChangeSerializer
from apps.accounts.util import parse_field_errors, create_form_field_error
from rest_framework.response import Response

UserModel = get_user_model()


class ChangeEmailView(GenericAPIView):
    serializer_class = EmailChangeSerializer
    permission_classes = (IsAuthenticated,)
    throttle_scope = 'api'

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response(parse_field_errors(e), status=status.HTTP_400_BAD_REQUEST)

        current_email = request.data['current_email']
        password = request.data['current_password']
        new_email = request.data['new_email']

        if current_email == new_email:
            return create_form_field_error("invalid", "new_email", "EMAIL_THE_SAME")

        user = authenticate(request=request, email=current_email, password=password)

        if user is None:
            return create_form_field_error("invalid", "password", "WRONG_PASSWORD")

        user.email = request.data['new_email']
        user.save()

        '''
        Create new email address and assign it to the user

        After confirmation all stale email addresses should be removed
        '''
        EmailAddress.objects.add_email(request, user, new_email, confirm=True)

        return JsonResponse({
            'status': 'success',
            'data': {
                'user': {
                    'email': self.request.user.email,
                    'isVerified': EmailAddress.objects.filter(email=self.request.user.email, verified=True).exists(),
                },
            }
        })
