from django.db import models

from django.conf import settings

# Create your models here.

User=settings.AUTH_USER_MODEL #Auth.user

class Product(models.Model):
    # owner=models.ForeignKey(User)
    user=models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        print(type(self.price))

        x = float(self.price)
        print(type(x))
        num = x * 0.8
        return "%.2f" % num
    @property
    def get_discount(self):
        return "122"
