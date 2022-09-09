from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body  # byte string of JSON Data
    data = {}
    try:
        data = json.loads(body) # String of json data--> Python Dict
    except:
        pass

    print(data.keys())
    print(body)
    return JsonResponse(data)
