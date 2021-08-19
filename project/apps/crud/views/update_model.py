from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.apps import apps


class UpdateModelView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            data = self.request.data
            fields = data['data']
            row_id = fields['id']

            model = data['model']
            app_label = data['package'].replace('.models', '').replace('apps.', '')
            model_class = apps.get_model(app_label=app_label, model_name=model)

            fields.pop('id', None)

            print(fields)

            model_class.objects.filter(pk=row_id).update(**fields)

            print(model_class)

            return JsonResponse({'status': 'success', 'data': {
                'updated_id': row_id
            }})

        return JsonResponse({'status': 'error', 'data': 'unauthenticated'})
