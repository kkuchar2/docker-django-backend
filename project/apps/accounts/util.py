def parse_field_errors(e):
    response = {
        'status': 'error',
        'data': {
            'form': {}  # The context for response errors is 'form'
        }
    }

    for key in e.detail:
        key_errors = e.detail[key]
        key_codes = []

        for i in range(0, len(key_errors)):
            key_codes.append({
                "code": key_errors[i].code,
                "message": str(key_errors[i])
            })

        response['data']['form'][key] = key_codes

    return response
