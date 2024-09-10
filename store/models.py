from django.db import models
from django.contrib.auth import get_user_model

from books.models import BookModel
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user_cart', blank=True, null=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_detail', on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel, on_delete=models.CASCADE)
    qauntity = models.PositiveSmallIntegerField()
    price = models.PositiveIntegerField()
    total_price = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.book.title}"


