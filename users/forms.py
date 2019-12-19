from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    institution_code = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    
    class Meta:
        # specifies that the model to be affected is the User model
        model = User

        # specifies the fields that will be displayed
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'institution_code']