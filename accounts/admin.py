from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['username', 'age', 'email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age',)}),
    )

    add_fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)    