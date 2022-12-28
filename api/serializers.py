from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# We import entire module to avoid circular Import problem
# from products.serializers import ProductSerializer
import products.serializers


class UserProductInlineSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # this_is_not_real = serializers.CharField(read_only=True)

    # other_products=serializers.SerializerMethodField(read_only=True)
    #     # request=self.context.get('request')
    #     # print(obj)
    #     user=obj
    #     #only five products
    #     my_products_qs=user.product_set.all()[:5]
    #     return UserProductInlineSerializer(my_products_qs,many=True,context=self.context).data

#
# class UserPublicSerializer(serializers.Serializer):
#     username = serializers.CharField(read_only=True)
#     id = serializers.IntegerField(read_only=True)
#     # this_is_not_real = serializers.CharField(read_only=True)
#
#     # other_products=serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'this_is_not_real',
#             'id'
#         ]
#
#     def create(self, validated_data):
#         user=User.objects.create(**validated_data)
#         return super().create(self, validated_data)
#
#     def update(self, instance, validated_data):
#         return super().update(self, instance, validated_data)
#     # def get_other_products(self,obj):
#     #     # request=self.context.get('request')
#     #     # print(obj)
#     #     user=obj
#     #     #only five products
#     #     my_products_qs=user.product_set.all()[:5]
#     #     return UserProductInlineSerializer(my_products_qs,many=True,context=self.context).data
