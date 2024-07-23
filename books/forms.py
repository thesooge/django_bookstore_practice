
from django.forms import ModelForm

from .models import BookModel

class CreateForm(ModelForm):
    class Meta:
        model = BookModel
        fields = ['title', 'description', 'author', 'price','cover',]

