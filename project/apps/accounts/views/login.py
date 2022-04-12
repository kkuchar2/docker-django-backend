from allauth.account.models import EmailAddress
from dj_rest_auth.utils import jwt_encode
from dj_rest_auth.views import LoginView
from django.contrib.auth.models import update_last_login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.accounts.util import parse_field_errors


class CustomLoginView(LoginView):

    def login(self):
        self.user = self.serializer.validated_data['user']
        self.access_token, self.refresh_token = jwt_encode(self.user)
        update_last_login(None, self.user)

    @method_decorator(ensure_csrf_cookie, name='dispatch')
    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)

        try:
            self.serializer.is_valid(raise_exception=True)
        except EmailAddress.DoesNotExist as e:
            return Response("EMAIL_DOES_NOT_EXIST", status=status.HTTP_401_UNAUTHORIZED)
        except ValidationError as e:
            return Response(parse_field_errors(e), status=status.HTTP_400_BAD_REQUEST)

        self.login()
        return self.get_response()
