from django.contrib import admin
from .models import BookModel, Comments

# Register your models here.

admin.site.register(BookModel)
admin.site.register(Comments)
