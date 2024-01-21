from django.urls import path
from .views import submit_review

urlpatterns = [
    path('<int:group_id>/<int:movie_id>/reviews/', submit_review, name='submit_review'),
]