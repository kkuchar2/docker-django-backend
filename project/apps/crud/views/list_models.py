import django.apps
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from settings.settings import AVAILABLE_MODELS


class ListModelsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:

            models = django.apps.apps.get_models()
            target_models = []

            for model in models:

                simple_name = model.__name__
                package = model.__module__
                full_package_name = "{}.{}".format(package, simple_name)

                if full_package_name in AVAILABLE_MODELS:
                    target_models.append({'package': package, 'model': simple_name})

            return Response(target_models, status=status.HTTP_200_OK)

        return JsonResponse({'status': 'error', 'data': 'Not authenticated'})
