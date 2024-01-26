from django.db import models
from accounts.models import CustomUser
from movies.models import MovieDetails

# Create your models here.


class ReviewGroups(models.Model):
    """
    Represents a review group for movies.

    Each group has a unique identifier (group_id)
      and is associated with a name (group_name).
    A group can have a description (group_description)
      providing additional information.
    It includes a ManyToMany relationship with movies (group_movies)
      and users (group_members).
    The creator of the group is tracked through the
      ForeignKey relationship (group_creator).

    Methods:
        - __str__: Returns the group_name for a
                   human-readable representation.
    """
    group_id = models.AutoField(
        primary_key=True
    )
    group_name = models.CharField(
        max_length=120,
        unique=True,
        blank=False,
        null=False
    )
    group_description = models.TextField(
        max_length=500,
        blank=True,
        null=True
    )
    group_movies = models.ManyToManyField(
        MovieDetails
    )
    group_members = models.ManyToManyField(
        CustomUser,
        related_name='user_groups_membership'
    )
    group_creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='created_groups',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.group_name
