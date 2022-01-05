import json

from allauth.account.adapter import get_adapter
from allauth.account.models import EmailConfirmationHMAC
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

'''
View that allows unauthenticated person 
that has confirmation link from email to confirm their email
after registration
'''


class ConfirmEmailView(APIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        self.object = confirmation = EmailConfirmationHMAC.from_key(data["token"])

        if confirmation.email_address.verified:
            return JsonResponse({'status': 'success', 'data': 'ALREADY_VERIFIED'})

        confirmation.confirm(self.request)
        confirmation.user.is_active = True
        confirmation.user.save()

        if self.request.user.is_authenticated and self.request.user.pk != confirmation.email_address.user_id:
            get_adapter(self.request).logout(self.request)
            return JsonResponse({'status': 'ACCOUNT_CONFIRMED_MESSAGE'})
        else:
            return JsonResponse({'status': 'ACCOUNT_CONFIRMED_MESSAGE'})
