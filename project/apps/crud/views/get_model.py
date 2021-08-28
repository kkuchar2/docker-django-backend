from django.apps import apps
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.accounts.serializers import UserSerializer
from apps.accounts.serializers import UserProfileSerializer
from apps.covid.serializers import CovidStatsSerializer, CovidCalcsSerializer

serializers = {
    'accounts.User': UserSerializer,
    'accounts.UserProfile': UserProfileSerializer,
    'covid.CovidStats': CovidStatsSerializer,
    'covid.CovidCalcs': CovidCalcsSerializer,
}


class GetModelView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_model_and_serializer(request_data):
        app_label = request_data['package'].replace('.models', '').replace('apps.', '')
        model_class = apps.get_model(app_label=app_label, model_name=request_data['model'])
        serializer = serializers["{}.{}".format(app_label, request_data['model'])]
        return [model_class, serializer]

    @staticmethod
    def create_headers_dict(model, serializer):
        serializer_meta = serializer.Meta

        fields = serializer_meta.fields

        try:
            editable_fields = serializer_meta.editable_fields
        except AttributeError:
            editable_fields = []

        final_fields = []

        for field in fields:
            final_fields.append({
                'name': field,
                'type': model._meta.get_field(field).get_internal_type(),
                'isEditable': field in editable_fields
            })

        return final_fields

    def build_response(self, header_fields, serializer):
        return {
            'package': self.request.data['package'],
            'model': self.request.data['model'],
            'headers': header_fields,
            'rows': serializer.data
        }

    def process_range_query(self, model, serializer, start_idx, end_idx):
        obj = model.objects.filter(pk__lte=end_idx, pk__gte=start_idx)
        sr = serializer(obj, many=True)
        header_fields = self.create_headers_dict(model, serializer)
        return JsonResponse({'status': 'success', 'data': self.build_response(header_fields, sr)})

    def process_single_item_query(self, model, serializer, idx):
        obj = model.objects.filter(pk__lte=idx, pk__gte=idx)
        sr = serializer(obj, many=True)
        header_fields = self.create_headers_dict(model, serializer)
        return JsonResponse({'status': 'success', 'data': self.build_response(header_fields, sr)})

    def process_all_data_query(self, model, serializer):
        obj = model.objects.all()
        sr = serializer(obj, many=True)
        header_fields = self.create_headers_dict(model, serializer)
        return JsonResponse({'status': 'success', 'data': self.build_response(header_fields, sr)})

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            print(self.request.data)

            data = self.request.data

            if 'model' not in data or 'package' not in data:
                return JsonResponse({'status': 'error', 'data': 'Missing `model` or `package` value in request'})

            app_model, serializer = self.get_model_and_serializer(data)

            print(serializer)

            if 'startIdx' in data and 'endIdx' in data:
                return self.process_range_query(app_model, serializer, data['startIdx'], data['endIdx'])

            if 'idx' in data and data['idx'] is not None:
                return self.process_single_item_query(app_model, serializer, data['idx'])

            return self.process_all_data_query(app_model, serializer)

        return JsonResponse({'status': 'error', 'data': 'Not authenticated'})