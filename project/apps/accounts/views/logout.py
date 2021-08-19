from django.conf import settings
from django.contrib.auth import logout as django_logout
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class LogoutView(APIView):
    permission_classes = (AllowAny,)
    throttle_scope = 'dj_rest_auth'

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass

        django_logout(request)

        from rest_framework_simplejwt.exceptions import TokenError
        from rest_framework_simplejwt.tokens import RefreshToken

        cookie_name = getattr(settings, 'JWT_AUTH_COOKIE', None)

        response = JsonResponse({'status': 'success'})

        from dj_rest_auth.jwt_auth import unset_jwt_cookies
        unset_jwt_cookies(response)

        if 'rest_framework_simplejwt.token_blacklist' in settings.INSTALLED_APPS:
            # add refresh token to blacklist
            try:
                token = RefreshToken(request.data['refresh'])
                token.blacklist()
            except KeyError:
                response.data = {'detail': _('Refresh token was not included in request data.')}
                response.status_code = status.HTTP_401_UNAUTHORIZED
            except (TokenError, AttributeError, TypeError) as error:
                if hasattr(error, 'args'):
                    if 'Token is blacklisted' in error.args or 'Token is invalid or expired' in error.args:
                        response.data = {'detail': _(error.args[0])}
                        response.status_code = status.HTTP_401_UNAUTHORIZED
                    else:
                        response.data = {'detail': _('An error has occurred.')}
                        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

                else:
                    response.data = {'detail': _('An error has occurred.')}
                    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

        elif not cookie_name:
            message = _(
                'Neither cookies or blacklist are enabled, so the token '
                'has not been deleted server side. Please make sure the token is deleted client side.',
            )
            response.data = {'detail': message}
            response.status_code = status.HTTP_200_OK

        return response
