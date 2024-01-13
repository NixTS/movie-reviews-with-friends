import requests
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime, timedelta
from moviestar.settings import TMDB_API_KEY
from .models import MovieDetails

# Create your views here.

BASE_URL = 'https://api.themoviedb.org/3/'

def list_of_movies(request):
    cached_movies = cache.get('cached_movies')
    
    if cached_movies is not None:
        movies = cached_movies
    else:
        url = f'{BASE_URL}movie/popular?api_key={TMDB_API_KEY}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            movies = []
            for movie in data.get('results', []):
                movie_id = movie.get('id')
                if movie_id:
                    movie_title = movie.get('title', '')
                    movie_poster = movie.get('poster_path', '')
                    movie_description = movie.get('overview', '')
                    genre_ids = movie.get('genre_ids', [])
                    movie_genre = fetch_genre_names(genre_ids)
                    movie_release_date = datetime.strptime(movie.get('release_date', ''), '%Y-%m-%d').date()
                    movie_length = timedelta(minutes=movie.get('runtime', 0))

                    movie_details, created = MovieDetails.objects.get_or_create(
                        movie_id=movie_id,
                        defaults={
                            'movie_title': movie_title,
                            'movie_poster': movie_poster,
                            'movie_description': movie_description,
                            'movie_genre': movie_genre,
                            'movie_release_date': movie_release_date,
                            'movie_length': movie_length,
                        }
                    )

                    if not created:
                        movie_details.movie_title = movie_title
                        movie_details.movie_poster = movie_poster
                        movie_details.movie_description = movie_description
                        movie_details.movie_genre = movie_genre
                        movie_details.movie_release_date = movie_release_date
                        movie_details.movie_length = movie_length
                        movie_details.save()

                    movies.append(movie_details)

            cache.set('cached_movies', movies, timeout=60*60*12)  

        else:
            print(f"Error fetching data from TMDB API. Status code: {response.status_code}")
            return HttpResponse(f"Error fetching data from TMDB API. Status code: {response.status_code}", status=response.status_code)

    return render(request, 'movies/list_of_movies.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(MovieDetails, movie_id=movie_id)
    return render(request, 'movies/movie_details.html', {'movie': movie})


def fetch_genre_names(genre_ids):
    genre_url = f'{BASE_URL}genre/movie/list?api_key={TMDB_API_KEY}'
    response = requests.get(genre_url)
    if response.status_code == 200:
        genres_data = response.json().get('genres', [])
        genre_names = [genre['name'] for genre in genres_data if genre['id'] in genre_ids]
        return genre_names
    return []