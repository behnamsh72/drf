from django.urls import  path
from . import views

#/api/products/
urlpatterns=[


    # path('',views.product_create_view),

    path('',views.product_list_create_view),

    # Primary key (pk)
    path('<int:pk>/',views.ProductDetailAPIView.as_view())
    #ANother method of implementing
    # path('<int:pk>/', views.ProductDetailAPIView)


    #Just for all in one method we implemented in this way:
    # path('',views.product_alt_view),
    # path('<int:pk>/',views.product_alt_view)

]