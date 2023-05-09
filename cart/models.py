from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# still needs the add_item to be implemented so that admin panel and elsewhere add_item is used


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, through="CartItem")
    total_quantity = models.PositiveIntegerField()

    # prevent creating duplicate CartItems with the same product for a Cart
    def add_item(self, product, quantity=1):
        try:
            cart_item = self.cartitem_set.get(product=product)
            cart_item.quantity += quantity
            cart_item.save()
        except CartItem.DoesNotExist:
            cart_item = CartItem.objects.create(
                cart=self, product=product, quantity=quantity)
        return cart_item


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
