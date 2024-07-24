
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BookList.as_view(), name='book-list'),
    path('<int:pk>', views.BookDetail, name='book-detail'),
    path('<int:pk>/update', views.UpdateBook.as_view(), name='book-update'),
    path('<int:pk>/delete',views.BookDelete.as_view(), name='book-delete'),
    path('add/', views.BookAdd.as_view(), name='book-add'),

]