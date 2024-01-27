from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from accounts.models import CustomUser
from movies.models import MovieDetails
from review_groups.models import ReviewGroups


class Review(models.Model):
    """
    Model for storing user reviews.

    This model represents user reviews for movies within specified groups.

    Attributes:
        - review_id (AutoField): Auto-incremented primary key for each review.
        - review_user (ForeignKey): User providing the review,
          linked to the CustomUser model.
        - review_movie (ForeignKey): Movie being reviewed,
          linked to the MovieDetails model.
        - review_group (ForeignKey): Group associated with the review,
          linked to the ReviewGroups model (nullable).
        - review_rating (IntegerField): Numerical rating provided by the user.
        - review_title (CharField): Title of the review, a short description.
        - review_text (TextField): Full text of the review.
    """
    review_id = models.AutoField(
        primary_key=True
    )
    review_user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    review_movie = models.ForeignKey(
        MovieDetails,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    review_group = models.ForeignKey(
        ReviewGroups,
        on_delete=models.CASCADE,
        related_name='group_reviews',
        null=True,
        blank=True
    )
    review_rating = models.IntegerField(
        default=1, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    review_title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
    )
    review_text = models.TextField(
        max_length=20000,
        blank=False,
        null=False,
    )

    class Meta:
        unique_together = ('review_user', 'review_movie', 'review_group')
        ordering = ["-review_id"]
