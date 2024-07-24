from django.shortcuts import render, reverse, redirect, get_object_or_404

from django.views import generic
from .forms import CreateForm, CommentForm

from .models import BookModel, Comments

# Create your views here.

class BookList(generic.ListView):
    model = BookModel
    template_name = 'books/book-list.html'
    context_object_name = 'book'
    paginate_by = 4

class UpdateBook(generic.UpdateView):
    model = BookModel 
    template_name = 'books/book-update.html'
    context_object_name = 'book' 
    fields = ['title', 'description', 'author', 'cover']

# class BookDetail(generic.DetailView):
#     model = BookModel 
#     template_name = 'books/book-detail.html'
#     context_object_name = 'book'     

def BookDetail(request, pk):
    book = get_object_or_404(BookModel, pk=pk)

    book_comments = book.comments.all()

    if request.method == 'POST':
        commnet_form = CommentForm(request.POST)
        if commnet_form.is_valid():
            comment = commnet_form.save(commit=False)
            comment.book = book
            comment.writer = request.user 
            comment.save()
            commnet_form = CommentForm()
        
    else:
        commnet_form = CommentForm()


    return render(request, 'books/book-detail.html', {'book' : book, 'comments': book_comments, 'form' : commnet_form})


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
    fields = ['title', 'description', 'author', 'price','cover',]

