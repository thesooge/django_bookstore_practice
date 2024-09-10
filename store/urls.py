
from django.urls import path
from . import views


urlpatterns = [
    path('', views.cart_view, name='cart_view'),
    path('addcart/<int:book_id>', views.add_cart, name='cart_add'),

]