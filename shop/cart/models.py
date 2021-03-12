from django.db import models

from user.models import User
from product.models import Product


class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.PositiveIntegerField()  # @TODO implement
    active = models.BooleanField(default=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,
                             related_name='items')
