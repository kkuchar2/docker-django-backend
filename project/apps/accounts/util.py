from rest_framework import status
from rest_framework.response import Response


def parse_field_errors(e):
    response = {
        'form': {}
    }

    for key in e.detail:
        key_errors = e.detail[key]
        key_codes = []

        for i in range(0, len(key_errors)):
            key_codes.append({
                "code": key_errors[i].code,
                "message": str(key_errors[i])
            })

        response['form'][key] = key_codes

    return response


def create_form_error(code, message):
    return Response({
        'form': {
            'non_field_errors': [
                {
                    "code": code,
                    "message": message
                }
            ]
        }
    }, status=status.HTTP_400_BAD_REQUEST)


def create_form_field_error(code, field_id, message):
    return Response({
        'form': {
            field_id: [
                {
                    "code": code,
                    "message": message
                }
            ]
        }
    }, status=status.HTTP_400_BAD_REQUEST)
