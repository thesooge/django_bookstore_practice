from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age','email') # fields should be filled in this form 


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser     
        fields = UserChangeForm.Meta.fields

