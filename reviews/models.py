from django.db import models

from django.db import models
from accounts.models import CustomUser
from movies.models import MovieDetails
from review_groups.models import ReviewGroups

# Create your models here.

class Review(models.Model):
    review_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reviews')
    review_movie = models.ForeignKey(MovieDetails, on_delete=models.CASCADE, related_name='reviews')
    review_group = models.ForeignKey(ReviewGroups, on_delete=models.CASCADE, related_name='group_reviews', null=True, blank=True)
    review_rating = models.IntegerField()
    review_text = models.TextField(max_length=20000, blank=True, null=True)

    class Meta:
        unique_together = ('review_user', 'review_movie', 'review_group')