from django.db import models
from accounts.models import CustomUser
from movies.models import MovieDetails

# Create your models here.

class ReviewGroups(models.Model):
    group_id = models.IntegerField(unique=True)
    group_name = models.CharField(max_length=120, unique=True, blank=False, null=False)
    group_description = models.TextField(max_length=500, blank=True, null=True)
    group_movies = models.ManyToManyField(MovieDetails)
    group_members = models.ManyToManyField(CustomUser, related_name='user_groups_membership')

    def __str__(self):
        return self.name