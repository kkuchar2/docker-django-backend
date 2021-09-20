from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.apps import apps


class DeleteModelDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            data = self.request.data

            print(data)

            model = data['model']
            app_label = data['package'].replace('.models', '').replace('apps.', '')
            model_class = apps.get_model(app_label=app_label, model_name=model)
            ids = data['rows']

            model_class.objects.filter(id__in=ids).delete()

            return JsonResponse({'status': 'success', 'data': {
                'package': data['package'],
                'model': model,
                'removedIds': ids
            }})

        return JsonResponse({'status': 'error', 'data': 'unauthenticated'})
