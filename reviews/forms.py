from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    Form for capturing user reviews of movies within a review group.

    This form is used to collect user reviews, including the rating, title, and
    text content. It is designed to be used within the context of a specific
    movie within a review group.

    Attributes:
        - review_rating (IntegerField): Numerical rating provided by the user.
        - review_title (CharField): Title of the review.
        - review_text (TextField): Text of the review.
    """
    class Meta:
        model = Review
        fields = ['review_rating', 'review_title', 'review_text']
