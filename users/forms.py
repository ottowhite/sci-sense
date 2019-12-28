from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    date_of_birth = forms.DateField(required=True, help_text='Format: YYYY-MM-DD; Example: 2003-04-30')
    is_staff = forms.BooleanField(required=False, label='I am a teacher')
    
    class Meta:
        # specifies that the model to be affected is the User model
        model = User

        # specifies the fields that will be displayed
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth', 'is_staff']