import json
import random
import string

from allauth.account.models import EmailConfirmationHMAC
from allauth.account.utils import complete_signup
from allauth.account.views import ConfirmEmailView
from django.contrib.auth import (logout as django_logout, get_user_model)
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_auth.app_settings import create_token
from rest_auth.registration.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_auth.serializers import TokenSerializer, UserDetailsSerializer
from rest_auth.views import LogoutView, PasswordResetView
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from apps.accounts.serializers import PasswordResetSerializer
from settings import settings


class SessionView(APIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return JsonResponse({
                'status': 'success',
                'data': {
                    'user': self.request.user.email
                }
            })
        else:
            return JsonResponse({'status': 'error', 'data': 'Not authenticated'})


class HelloView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        print("Hello: {}".format(request.user))
        msg = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        content = {'message': msg}
        return JsonResponse(content)


def parse_field_errors(e):
    response = {
        'status': 'error',
        'data': {}
    }

    for key in e.detail:
        key_errors = e.detail[key]
        key_codes = []

        data = []

        for i in range(0, len(key_errors)):
            key_codes.append({
                "code": key_errors[i].code,
                "message": str(key_errors[i])
            })

        response['data'][key] = key_codes

    return response


class CustomResetPasswordView(PasswordResetView):
    """
        Calls Django Auth PasswordResetForm save method.

        Accepts the following POST parameters: email
        Returns the success/fail message.
        """
    serializer_class = PasswordResetSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        # Create a serializer with request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        # Return the success message with OK HTTP status
        return JsonResponse({'status': 'success', 'data': {"message": "Email withjj code sent"}})


class CustomRegisterView(RegisterView):

    def get_response_data(self, user):
        return {'status': '0'}

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            response = parse_field_errors(e)
            print('Response: {}'.format(response))
            return JsonResponse(response)

        user = serializer.save(self.request)
        create_token(self.token_model, user, serializer)

        try:
            complete_signup(self.request, user, settings.ACCOUNT_EMAIL_VERIFICATION, None)
        except Exception as e:
            user.delete()
            raise e

        return JsonResponse({'status': 'success', 'data': {}})


class CustomLoginView(LoginView):
    authentication_classes = (TokenAuthentication,)

    def get_response_serializer(self):
        return TokenSerializer

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.token = create_token(self.token_model, self.user, self.serializer)
        self.process_login()

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data, context={'request': request})
        try:
            self.serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            response = parse_field_errors(e)
            print('Response: {}'.format(response))
            return JsonResponse(response)

        self.login()
        return self.get_response()

    def get_response(self):
        serializer = TokenSerializer(instance=self.token, context={'request': self.request})
        print("Serializer data: {}".format(serializer.data))
        return JsonResponse({'status': 'success', 'data': {
            'key': serializer.data["key"],
            'user': self.user.email
        }})


class CustomConfirmEmailView(ConfirmEmailView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        self.object = confirmation = EmailConfirmationHMAC.from_key(data["key"])

        if confirmation.email_address.verified:
            return JsonResponse({'status': 'already_verified'})

        confirmation.confirm(self.request)

        if self.request.user.is_authenticated and self.request.user.pk != confirmation.email_address.user_id:
            self.logout()
            return JsonResponse({'status': 'confirmed_and_logged_out'})
        else:
            return JsonResponse({'status': 'confirmed'})


class UserDetailsView(RetrieveUpdateAPIView):
    """
    Reads and updates UserModel fields
    Accepts GET, PUT, PATCH methods.

    Default accepted fields: username, first_name, last_name
    Default display fields: pk, username, email, first_name, last_name
    Read-only fields: pk, email

    Returns UserModel fields.
    """
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()


class CustomLogoutView(LogoutView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        django_logout(request)

        return JsonResponse({'status': 'success'})


class DeleteAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.request.user.delete()
            return JsonResponse({'status': 'success', 'data': 'Deleted user'})
