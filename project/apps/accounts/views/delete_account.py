from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class DeleteAccountView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.request.user.delete()
            return JsonResponse({'status': 'success', 'data': 'Deleted user'})
