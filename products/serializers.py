from rest_framework import serializers
from .models import Product
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from . import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)

    # related_products=ProductInlineSerializer(source='user.product_set.all',read_only=True,many=True)
    # Instad of user field we can declare user as serializer method field
    # my_user_data=serializers.SerializerMethodField(read_only=True)
    # my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    title = serializers.CharField(validators=[validators.validate_title_no_hello, validators.unique_product_title])

    # i don't wanna user related data such as this
    # email=serializers.EmailField(source='user.email',read_only=True)
    # name=serializers.CharField(source='title',read_only=True)
    class Meta:
        model = Product
        # fields = ['title', 'content', 'price', 'sale_price', 'get_discount']

        fields = ['owner',
                  # 'email',
                  'pk', 'url', 'edit_url', 'title',
                  # 'name',
                  'content', 'price', 'sale_price','public',
                  # 'my_discount',
                  # 'my_user_data',
                  # 'related_products'
                  ]
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

    # Instad of user field we can declare user as serializer method field
    # def get_my_user_data(self, obj):
    #     return {"username": obj.user.username}

    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    #
    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount
