
from django.forms import ModelForm

from .models import BookModel, Comments

class CreateForm(ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'description', 'author', 'price','cover',]

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text', ]        

