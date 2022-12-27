from rest_framework import serializers

#We import entire module to avoid circular Import problem
# from products.serializers import ProductSerializer
import products.serializers


class UserProductInlineSerializer(serializers.Serializer):
    url=serializers.HyperlinkedIdentityField(view_name='product-detail',lookup_field='pk',read_only=True)
    title=serializers.CharField(read_only=True)

class UserPublicSerializer(serializers.Serializer):
    username=serializers.CharField(read_only=True)
    id=serializers.IntegerField(read_only=True)
    other_products=serializers.SerializerMethodField(read_only=True)

    def get_other_products(self,obj):
        # request=self.context.get('request')
        # print(obj)
        user=obj
        #only five products
        my_products_qs=user.product_set.all()[:5]
        return UserProductInlineSerializer(my_products_qs,many=True,context=self.context).data