from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class BookModel(models.Model):

    title = models.CharField(max_length=50)
    desctiption = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pricee = models.DecimalField(decimal_places=2, max_digits=6)


    def __str__(self):
        return f"{self.title}---{self.author}"
    
    def get_absolute_url(self):
        return reverse('book-detail' ,args=[self.id])
    
    