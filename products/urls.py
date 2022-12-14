from django.urls import  path
from . import views

#/api/products/
urlpatterns=[


    # path('',views.product_create_view),


    path('',views.product_list_create_view,name='product-list'),


    path('<int:pk>/update', views.ProductUpdateAPIView.as_view(),name="product-edit"),
    path('<int:pk>/delete', views.ProductDestroyAPIView.as_view()),

    # Primary key (pk)
    path('<int:pk>/',views.ProductDetailAPIView.as_view(),name='product-detail')
    #ANother method of implementing this
    # path('<int:pk>/', views.ProductDetailAPIView)


    #Just for all in one method we implemented in this way:
    # path('',views.product_alt_view),
    # path('<int:pk>/',views.product_alt_view)

    # replace product list create view with mixin view
    # path('', views.product_mixin_view),
    # path('<int:pk>/', views.product_mixin_view)

]