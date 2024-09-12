from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic

from .models import Cart, CartItem
from books.models import BookModel
from .forms import AddToCartForm
# Create your views here.

def get_cart(user):
    cart, created = Cart.objects.get_or_create(user=user)
    return cart


@login_required
def cart_view(request):
    cart = get_cart(request.user)

    return render(request, 'store/cart.html', {'cart':cart})

@login_required
def add_cart(request, book_id):

    book = get_object_or_404(BookModel,id=book_id)
    cart = get_cart(request.user)

    cart_item, created = CartItem.objects.get_or_create(cart= cart, book= book)

    if not created:
        cart_item.qauntity += 1
        cart_item.save()

    return redirect('cart_view')  

@login_required
def delete_cart(request, book_id):
    cart_item = get_object_or_404(CartItem,id=book_id)
    cart_item.delete()

    return redirect('cart_view')