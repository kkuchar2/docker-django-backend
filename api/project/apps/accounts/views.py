from allauth.account.views import ConfirmEmailView
from django.http import JsonResponse, Http404
from rest_auth.app_settings import create_token
from rest_auth.registration.views import LoginView
from rest_auth.registration.views import RegisterView
from rest_auth.serializers import TokenSerializer
from rest_framework import serializers
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


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

        self.perform_create(serializer)

        return JsonResponse({ 'status': 'success', 'data': {}})


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


class CustomConfirmEmailView(ConfirmEmailView):
    def get(self, *args, **kwargs):
        try:
            self.object = self.get_object()
            return self.post(*args, **kwargs)
        except Http404:
            self.object = None
            return JsonResponse({'status': 'error'})

    def post(self, *args, **kwargs):
        self.object = confirmation = self.get_object()

        if confirmation.email_address.verified:
            return JsonResponse({'status': 'already_verified'})

        confirmation.confirm(self.request)

        if self.request.user.is_authenticated and self.request.user.pk != confirmation.email_address.user_id:
            self.logout()
            return JsonResponse({'status': 'confirmed_and_logged_out'})
        else:
            return JsonResponse({'status': 'confirmed'})
