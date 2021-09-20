from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.apps import apps


class AddItemView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            data = self.request.data

            model_package = data['package']
            model = data['model']
            field_data = data['data']

            app_label = model_package.replace('.models', '').replace('apps.', '')
            model_class = apps.get_model(app_label=app_label, model_name=model)

            model_class.objects.create(**field_data)

            return JsonResponse({'status': 'success', 'data': {}})

        return JsonResponse({'status': 'error', 'data': 'unauthenticated'})
