from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Extension for the default user model.

    Attributes:
        - user_date_of_birth (DateField): Date of birth of the user.
        - user_bio (TextField): User's bio or additional information.

    Methods:
        - __str__(): Returns the username as the string representation of the user.

    Usage:
        - This model extends the default user model provided by Django to include
        additional fields such as date of birth and a bio.
    """
    user_date_of_birth = models.DateField(null=True, blank=True)
    user_bio = models.TextField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.username