from django.urls import path,include
from . import views
#from .views import api_home
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('auth/',obtain_auth_token),
    path('',views.api_home),
    # path('api/products/',include('products.urls'))

]