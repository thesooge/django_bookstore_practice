from typing import Iterable
from django.db import models
from django.contrib.auth import get_user_model

from books.models import BookModel
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_cart', blank=True, null=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    qauntity = models.PositiveSmallIntegerField(default=1)
    price = models.PositiveIntegerField(null=True, blank=True)
    total_price = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.book.title}"


class Order(models.Model):
    ORDER_STATUS = [
        ('up','UnPaid'),
        ('p','Paid'),
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='order_detail')
    status = models.CharField(max_length=255, choices=ORDER_STATUS)

    order_datetime_created = models.DateTimeField(auto_now_add=True)
    order_datetime_modified = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items',on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    price = models.IntegerField()
    total_price = models.FloatField(null=True, blank=True)

    def save(self):
        self.total_price = self.quantity * self.price

        super(OrderItem, self).save(*args, **kwargs)
     
        