from django import forms
from django.core.exceptions import ValidationError
from .models import User
from .validators import (
    password_length_validator,
    password_contains_number,
    password_contains_capital
)
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    
    first_name      = forms.CharField(required=True)
    last_name       = forms.CharField(required=True)
    date_of_birth   = forms.DateField(required=True, help_text='Format: YYYY-MM-DD; Example: 2003-04-30')
    is_staff        = forms.BooleanField(required=False, label='I am a teacher')
    email           = forms.EmailField(required=True)
    password1       = forms.CharField(
                        widget      = forms.PasswordInput, 
                        label       = 'Password',
                        validators  = [
                            password_length_validator,
                            password_contains_number,
                            password_contains_capital
                        ]
                    )
    password2       = forms.CharField(widget=forms.PasswordInput, label='Password confirmation')
    
    
    def clean_password2(self):
        password1 = self.data['password1']
        password2 = self.data['password2']

        if password1 != password2:
            raise ValidationError(f'{password1} and {password2} don\'t match')
        else:
            return password2
    
    
    class Meta:
        # specifies that the model to be affected is the User model
        model = User

        # specifies the fields that will be displayed
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'date_of_birth', 'is_staff']