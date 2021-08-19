import json

from allauth.account.adapter import get_adapter
from allauth.account.models import EmailConfirmationHMAC
from django.http import JsonResponse
from rest_framework.decorators import authentication_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny

'''
View that allows unauthenticated person 
that has confirmation link from email to confirm their email
after registration
'''


@authentication_classes([])
class ConfirmEmailView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        self.object = confirmation = EmailConfirmationHMAC.from_key(data["key"])

        if confirmation.email_address.verified:
            return JsonResponse({'status': 'success', 'data': 'already_verified'})

        confirmation.confirm(self.request)

        if self.request.user.is_authenticated and self.request.user.pk != confirmation.email_address.user_id:
            get_adapter(self.request).logout(self.request)
            return JsonResponse({'status': 'confirmed_and_logged_out'})
        else:
            return JsonResponse({'status': 'confirmed'})
