from django.shortcuts import render, get_object_or_404, redirect

from .models import Cart, CartItem
from books.models import BookModel
# Create your views here.

def cart_get(user):
    cart = Cart.objects.get_or_create(user=user)
    return cart

def cart_view(request):
    cart = cart_get(request.user)

    return render(request, 'store/cart.html', {'cart':cart})

def add_cart(request, book_id):

    book = get_object_or_404(BookModel, id=book_id)
    cart = cart_get(request.user)

    cart_item, created = CartItem.objects.get_or_create(cart= cart, book= book)

    if not created:
        cart_item.qauntity += 1
        cart_item.save()

    return redirect('cart_view')  




