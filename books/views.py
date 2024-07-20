from django.shortcuts import render, reverse

from django.views import generic

from .models import BookModel

# Create your views here.

class BookList(generic.ListView):
    model = BookModel
    template_name = 'books/book-list.html'
    context_object_name = 'book'

class UpdateBook(generic.UpdateView):
    model = BookModel 
    template_name = 'books/book-update.html'
    context_object_name = 'book' 
    fields = ['title', 'description', 'author', 'cover']

class BookDetail(generic.DetailView):
    model = BookModel 
    template_name = 'books/book-detail.html'
    context_object_name = 'book'     

class BookDelete(generic.DeleteView):
    model = BookModel
    template_name = 'books/book-delete.html'
    context_object_name = 'book'

    def get_success_url(self) -> str:
        return reverse('book-list')    
    
class BookAdd(generic.CreateView):
    model = BookModel
    template_name = 'books/book-add.html'
    context_object_name = 'book'    
    fields = ['title', 'description', 'author', 'price','cover']