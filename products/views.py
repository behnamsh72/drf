from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


# Create your views here.


# class ProductCreateApiView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def perform_create(self, serializer):
#         #serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         title=serializer.validated_data.get('title')
#         content=serializer.validated_data.get('title')
#         #or None
#         if content is None:
#             content=title
#
#         serializer.save(content=content)
#         #Send  a Django signal
#
#
# product_create_view=ProductCreateApiView.as_view()

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('title')
        #or None
        if content is None:
            content=title

        serializer.save(content=content)
        #Send  a Django signal


product_list_create_view=ProductListCreateApiView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    #Product.ob
#for second method
# product_detail_view=ProductDetailAPIView.as_view()


class ProductListApiView(generics.ListAPIView):

    """
    Not gonna use this method
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field='pk' ?

product_list_view=ProductListApiView.as_view()