from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from products.models import Product

# def api_home(request, *args, **kwargs):
#     print(request.GET) #url query params
#     print(request.POST)
#     body = request.body  # byte string of JSON Data
#     data = {}
#     try:
#         data = json.loads(body)  # String of json data--> Python Dict
#     except:
#         pass
#
#     print(data.keys())
#     print(body)
#     data['params']=dict(request.GET)
#     data['headers'] = dict(request.headers) # request.META
#     print(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id']=model_data.id
        data['title'] = model_data.title
        data['content']=model_data.content
        data['price']=model_data.price
        # model instance(model_data)
        # turn  a Python dict
        # return json to my client
        # this process called Serialization
    return JsonResponse(data)
