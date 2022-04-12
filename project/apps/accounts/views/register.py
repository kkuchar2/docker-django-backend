from allauth.account import signals
from allauth.account.utils import _has_verified_for_login, send_email_confirmation
from dj_rest_auth.registration.views import RegisterView
from rest_framework import serializers, status
from rest_framework.response import Response

from apps.accounts.util import parse_field_errors


class CustomRegisterView(RegisterView):

    def create(self, request, *args, **kwargs):

        # Validate request with serializer
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response(parse_field_errors(e), status=status.HTTP_400_BAD_REQUEST)

        # Create user
        user = serializer.save(self.request)

        # Notify user created
        signal_kwargs = {}

        signals.user_signed_up.send(
            sender=user.__class__,
            request=self.request._request,
            user=user,
            **signal_kwargs
        )

        # If email not already confirmed send confirmation E-amil
        if not _has_verified_for_login(user, None):
            send_email_confirmation(self.request._request, user, signup=True)
            return Response({'detail': 'Sent confirmation email'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Already verified'}, status=status.HTTP_400_BAD_REQUEST)
