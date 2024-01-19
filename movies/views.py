import requests
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from moviestar.settings import TMDB_API_KEY
from .models import MovieDetails
from review_groups.models import ReviewGroups

# Create your views here.

BASE_URL = 'https://api.themoviedb.org/3/'


def list_of_movies(request):
    cached_movies = cache.get('cached_movies')

    if cached_movies is not None:
        movies = cached_movies
    else:
        movies = fetch_movies_from_api()

    return render(request, 'movies/list_of_movies.html', {'movies': movies})


def fetch_movies_from_api():
    url = f'{BASE_URL}movie/popular?api_key={TMDB_API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = process_movie_data(data)
        cache.set('cached_movies', movies, timeout=60 * 60 * 12)
        return movies
    else:
        print(f"Error fetching data from TMDB API. Status code: {response.status_code}")
        return HttpResponse(f"Error fetching data from TMDB API. Status code: {response.status_code}",
                            status=response.status_code)


def process_movie_data(data):
    movies = []

    for movie in data.get('results', []):
        movie_details = process_movie_details(movie)
        movies.append(movie_details)

    return movies


def process_movie_details(movie):
    movie_id = movie.get('id')
    movie_title = movie.get('title', '')
    movie_poster = movie.get('poster_path', '')
    movie_description = movie.get('overview', '')
    genre_ids = movie.get('genre_ids', [])
    movie_genre = fetch_genre_names(genre_ids)
    movie_release_date = datetime.strptime(movie.get('release_date', ''), '%Y-%m-%d').date()
    movie_duration = timedelta(minutes=movie.get('runtime', 0))

    movie_details, created = MovieDetails.objects.get_or_create(
        movie_id=movie_id,
        defaults={
            'movie_title': movie_title,
            'movie_poster': movie_poster,
            'movie_description': movie_description,
            'movie_genre': movie_genre,
            'movie_release_date': movie_release_date,
            'movie_duration': movie_duration,
        }
    )

    if not created:
        update_existing_movie_details(movie_details, movie_title, movie_poster, movie_description, movie_genre,
                                      movie_release_date, movie_duration)

    return movie_details


def update_existing_movie_details(movie_details, movie_title, movie_poster, movie_description, movie_genre,
                                  movie_release_date, movie_duration):
    movie_details.movie_title = movie_title
    movie_details.movie_poster = movie_poster
    movie_details.movie_description = movie_description
    movie_details.movie_genre = movie_genre
    movie_details.movie_release_date = movie_release_date
    movie_details.movie_duration = movie_duration
    movie_details.save()


def fetch_genre_names(genre_ids):
    genre_url = f'{BASE_URL}genre/movie/list?api_key={TMDB_API_KEY}'
    response = requests.get(genre_url)

    if response.status_code == 200:
        genres_data = response.json().get('genres', [])
        genre_names = [genre['name'] for genre in genres_data if genre['id'] in genre_ids]
        return genre_names

    return []



def movie_detail(request, movie_id):
    movie = get_object_or_404(MovieDetails, movie_id=movie_id)
    groups = ReviewGroups.objects.all()  # Retrieve all groups

    if request.method == 'POST':
        return add_movie_to_group(request, movie_id)

    return render(request, 'movies/movie_details.html', {'movie': movie, 'groups': groups, 'back_url': reverse('movies'), 'movie_id': movie_id})


def add_movie_to_group(request, movie_id):
    if request.method == 'POST':
        group_id = request.POST.get('group_id')
        movie = get_object_or_404(MovieDetails, movie_id=movie_id)
        group = get_object_or_404(ReviewGroups, group_id=group_id)

        # Add the movie to the group
        group.group_movies.add(movie)

        # Redirect to the movie details page
        return HttpResponseRedirect(reverse('movie_details', args=[movie_id]))