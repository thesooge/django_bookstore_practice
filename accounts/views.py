from django.shortcuts import render, reverse

from django.views import generic

from .models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm

# Create your views here.

class SignUp(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    model = CustomUser

    def get_success_url(self) -> str:
        return reverse('login')
    