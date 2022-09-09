from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    print(request.GET) #url query params
    print(request.POST)
    body = request.body  # byte string of JSON Data
    data = {}
    try:
        data = json.loads(body)  # String of json data--> Python Dict
    except:
        pass

    print(data.keys())
    print(body)
    data['params']=dict(request.GET)
    data['headers'] = dict(request.headers) # request.META
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)
