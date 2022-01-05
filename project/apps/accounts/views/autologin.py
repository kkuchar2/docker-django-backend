from allauth.account.models import EmailAddress
from django.http import JsonResponse
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from apps.accounts.serializers.avatar_serializer import AvatarSerializer


class AutoLoginView(APIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            s = AvatarSerializer()

            return JsonResponse({
                'status': 'success',
                'data': {
                    'user': {
                        'email': self.request.user.email,
                        'is_staff': self.request.user.is_staff,
                        'isVerified': EmailAddress.objects.filter(email=self.request.user.email, verified=True).exists(),
                        'avatar': s.get_avatar_url(self.request, self.request.user)
                    },
                }
            })
        else:
            return JsonResponse({'status': 'error', 'data': 'Not authenticated'})
