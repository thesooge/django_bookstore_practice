from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class BookModel(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    author = models.CharField(max_length=50, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    cover = models.ImageField(upload_to='book_covers/', blank=True)
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)



    def __str__(self):
        return f"{self.title}---{self.author}"
    
    def get_absolute_url(self):
        return reverse('book-detail' ,args=[self.id])
