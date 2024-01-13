import requests
from django.shortcuts import render
from django.http import HttpResponse
from moviestar.settings import TMDB_API_KEY
from .models import MovieDetails

# Create your views here.

BASE_URL = 'https://api.themoviedb.org/3/'

def list_of_movies(request):
    url = f'{BASE_URL}movie/popular?api_key={TMDB_API_KEY}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(data)

        for movie in data.get('results', []):
            movie_id = movie.get('id')
            if movie_id:
                movie_title = movie.get('title', '')
                movie_poster = movie.get('poster_path', '')

                movie_details, created = MovieDetails.objects.get_or_create(
                    movie_id=movie_id,
                    defaults={
                        'movie_title': movie_title,
                        'movie_poster': movie_poster,
                    }
                )

                if not created:
                    movie_details.movie_title = movie_title
                    movie_details.movie_poster = movie_poster
                    movie_details.save()

        movies = MovieDetails.objects.all()
        return render(request, 'movies/list_of_movies.html', {'movies': movies})
    else:
        print(f"Error fetching data from TMDB API. Status code: {response.status_code}")
        return HttpResponse(f"Error fetching data from TMDB API. Status code: {response.status_code}", status=response.status_code)
