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


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'user_date_of_birth', 'user_bio']