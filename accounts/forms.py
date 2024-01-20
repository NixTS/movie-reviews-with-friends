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