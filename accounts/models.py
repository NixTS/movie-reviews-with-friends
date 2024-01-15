from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_date_of_birth = models.DateField(null=True, blank=True)
    user_bio = models.TextField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.username