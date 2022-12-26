from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse

from . import validators
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title=serializers.CharField(validators=[validators.validate_title_no_hello , validators.unique_product_title])
    # name=serializers.CharField(source='title',read_only=True)
    class Meta:
        model = Product
        # fields = ['title', 'content', 'price', 'sale_price', 'get_discount']
        fields = ['pk', 'url', 'edit_url', 'title','content', 'price', 'sale_price', 'my_discount']

        fields = ['pk', 'url', 'edit_url', 'title','content', 'price', 'sale_price', 'my_discount']
        # fields = ['pk', 'url', 'edit_url', 'title','name','content', 'price', 'sale_price', 'my_discount']

    #
    # def validate_title(self, value):
    #     requests=self.context.get('request')
    #     user=requests.user
    #     qs=Product.objects.filter(user=user,title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def get_my_discount(self,obj):
    #     try:
    #         return obj.get_discount
    #     except:
    #         return None

    # def create(self, validated_data):
    #     # return Product.objects.create(**validated_data)
    #     # email=validated_data.pop('email')
    #     obj= super().create(validated_data)
    #     # print(email,obj)
    #     return obj
    #
    # def update(self, instance, validated_data):
    #     email=validated_data.pop('email')
    #     instance.title=validated_data.get('title')
    #     return super().update(instance,validated_data)
    #

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount
