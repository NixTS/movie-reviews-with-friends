from django.urls import path
from movies.views import list_of_movies, movie_detail, add_movie_to_group

urlpatterns = [
    path('movies/', list_of_movies, name='movies'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_details'),
    path('movies/<int:movie_id>/add_to_group/', add_movie_to_group, name='add_movie_to_group'),
]