from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class RegistrationForm(UserCreationForm):
    """
    Custom registration form based on UserCreationForm.
    Extends the default user creation form.

    Attributes:
        - username: A required field for the username.
        - email: A required field for the email address.
        - password1: A required field for the user's password.
        - password2: A required field for confirming the password.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

        labels = {
            'username': 'Username',
            'email': 'E-Mail Adress',
            'password1': 'Password',
            'password2': 'Password confirmation'
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={
                'placeholder': 'E-Mail@Address.com'
            }),
        }


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'user_date_of_birth',
            'user_bio'
            ]

        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-Mail Adress',
            'user_date_of_birth': 'YYYY-MM-DD',
            'user_bio': 'Biography'
        }

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail Address'}),
            'user_date_of_birth':
            forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'}),
        }
