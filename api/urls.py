from django.urls import path,include
from . import views
#from .views import api_home

urlpatterns=[
    path('',views.api_home),
    # path('api/products/',include('products.urls'))
]