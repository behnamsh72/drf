from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

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


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data['id']=model_data.id
#         data['title'] = model_data.title
#         data['content']=model_data.content
#         data['price']=model_data.price
#         # model instance(model_data)
#         # turn  a Python dict
#         # return json to my client
#         # this process called Serialization
#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#         print(data)
#         json_data_str=json.dumps(data)
#     return HttpResponse(json_data_str,headers={"content-type":"application/json"})
#

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return JsonResponse(data)

##Using Response instead of JsonResponse
##change model_to_dict to a Custom Serializar
# @api_view(["GET", "POST"])

# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """ DRF API VIEW"""
#     #
#     # if request.method != "POST":
#     #     return Response({"detail": "GET NOT ALLOwed"}, status=405)
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data=ProductSerializer(instance).data
#     return Response(data)

# @api_view(["POST"])
# def api_home(request, *args, **kwargs):
#     """ DRF API VIEW"""
#     #
#     # if request.method != "POST":
#     #     return Response({"detail": "GET NOT ALLOwed"}, status=405)
#     data=request.data
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         data=ProductSerializer(instance).data
#     return Response(data)
#

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    :param request:
    :param args:
    :param kwargs:
    :return:
    """
    data = request.data
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance=serializer.save()
        #instance=form.save()
        print(serializer.data)
        data=serializer.data
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)

