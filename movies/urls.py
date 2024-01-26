from django.urls import path
from django.contrib.auth.decorators import login_required
from movies.views import list_of_movies, movie_detail, add_movie_to_group

urlpatterns = [
    path(
        'list_movies/',
        list_of_movies,
        name='movies'
    ),
    path(
        'details/<int:movie_id>/',
        movie_detail,
        name='movie_details'
    ),
    path(
        'movies/<int:movie_id>/add_to_group/',
        login_required(add_movie_to_group),
        name='add_movie_to_group'
    ),
]
