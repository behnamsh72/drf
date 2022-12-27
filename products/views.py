from rest_framework import generics, mixins, permissions
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404

from django.shortcuts import get_object_or_404

from cfehome.permissions import IsStaffEditorPermission

from api.mixins import StaffEditorPermissionMixin,UserQuerySetMixin


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

# if we use get method this function retriev all the products and
# if we use post method this function creates all the
class ProductListCreateApiView(UserQuerySetMixin,StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_staff_view=False

    # Because we defined it in the defaiult setting it's redundent
    # authentication_classes = [authentication.SessionAuthentication,
    #                           # authentication.TokenAuthentication
    #                           TokenAuthentication]
    # permission_classes = [permissions.DjangoModelPermissions]
    # commented because we extend this class from StaffEditorPermissionMixin
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('title')
        # or None
        if content is None:
            content = title

        serializer.save(user=self.request.user,content=content)  # just similar to form.save() or model.save()
        # Send  a Django signal

    #Commented because we inherit from api.mixin.UserQuerySetMixin
    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     requests = self.request
    #     user=requests.user
    #     if not user.is_authenticated:
    #         return Product.objects.none()
    #     print(requests.user)
    #     return qs.filter(user=requests.user)


product_list_create_view = ProductListCreateApiView.as_view()


class ProductDetailAPIView(UserQuerySetMixin,StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    allow_staff_view=False

    # commented because we extend this class from StaffEditorPermissionMixin
    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    # lookup_field = 'pk'
    # Product.ob


class ProductUpdateAPIView(UserQuerySetMixin,StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # commented because we extend this class from StaffEditorPermissionMixin

    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDestroyAPIView(UserQuerySetMixin, StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    # commented because we extend this class from StaffEditorPermissionMixin

    # permission_classes = [permissions.IsAdminUser,IsStaffEditorPermission]

    def perform_delete(self, instance):
        super().perform_destroy(instance)


# for second method
# product_detail_view=ProductDetailAPIView.as_view()


class ProductListApiView(generics.ListAPIView):
    """
    Not gonna use this method
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_list_view = ProductListApiView.as_view()


# Working with Mixnin
class ProductMixinView(UserQuerySetMixin,mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                       generics.GenericAPIView
    , StaffEditorPermissionMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):

        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "this is a single view doing cool stuff"
        serializer.save(content=content)


product_mixin_view = ProductMixinView.as_view()


# def post
# All In One
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == "GET":
        if pk is not None:
            # details view
            # queryset = Product.objects.filter(pk=pk)
            # if not queryset.exist():
            #     raise Http404
            # or we can use this method
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        else:
            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)
