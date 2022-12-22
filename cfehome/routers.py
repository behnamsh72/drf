from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet

from products.viewsets import ProductGenericViewSet

router=DefaultRouter()

#product_abc preappend path
# router.register('products',ProductViewSet,basename='products')
router.register('products',ProductGenericViewSet,basename='products')

urlpatterns= router.urls
print(router.urls)

