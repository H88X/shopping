from django.db import models
from shop.models import Product


class Cart(models.Model):
    cart_id = models.CharField(max_length=50, blank=True)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']

    def _str_(self):
         return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models .BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
         return self.product.price * self.quantity

    def _str_(self):
         return self.product