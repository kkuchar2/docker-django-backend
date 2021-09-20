from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
import django.apps

from settings.settings import AVAILABLE_MODELS


class ListModelsView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:

            models = django.apps.apps.get_models()

            target_models = []

            for model in models:

                simple_name = model.__name__
                package = model.__module__
                full_package_name = "{}.{}".format(package, simple_name)

                if full_package_name in AVAILABLE_MODELS:
                    target_models.append({'package': package, 'model': simple_name})

            return JsonResponse({'status': 'success', 'data': target_models})

        return JsonResponse({'status': 'error', 'data': 'Not authenticated'})
