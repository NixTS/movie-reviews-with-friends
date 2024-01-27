from django.urls import path
from django.contrib.auth.decorators import login_required
from moviestar.views import access_denied
from .views import submit_review, edit_review, delete_review

urlpatterns = [
    path(
        '<int:group_id>/<int:movie_id>/reviews/',
        login_required(submit_review),
        name='submit_review'
    ),
    path(
        '<int:group_id>/<int:movie_id>/<int:review_id>/edit_review',
        login_required(edit_review),
        name='edit_review'
    ),
    path(
        '<int:group_id>/<int:movie_id>/<int:review_id>/delete_review',
        login_required(delete_review),
        name='delete_review'
    ),
    path(
        'access_denied/',
        access_denied,
        name='access_denied'
    ),
]