from django.urls import path
from .views import submit_review, edit_review, delete_review

urlpatterns = [
    path('<int:group_id>/<int:movie_id>/reviews/', submit_review, name='submit_review'),
    path('<int:group_id>/<int:movie_id>/<int:review_id>/edit_review', edit_review, name='edit_review'),
    path('<int:group_id>/<int:movie_id>/<int:review_id>/delete_review', delete_review, name='delete_review'),
]