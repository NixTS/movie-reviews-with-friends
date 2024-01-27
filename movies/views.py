import requests
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, timedelta
from moviestar.settings import TMDB_API_KEY
from .models import MovieDetails
from review_groups.models import ReviewGroups
from accounts.models import CustomUser


BASE_URL = 'https://api.themoviedb.org/3/'


def list_of_movies(request):
    """
    Lists all movies from the popular endpoint.

    Checks for cached data. If cached data is available,
    it is used; otherwise, data is fetched from the API.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - Rendered HTML page with a list of movies.
    """
    cached_movies = cache.get('cached_movies')

    if cached_movies is not None:
        movies = cached_movies
    else:
        movies = fetch_movies_from_api()

    return render(request, 'movies/list_of_movies.html', {'movies': movies})


def fetch_movies_from_api():
    """
    Fetches a list of popular movies from The Movie Database (TMDB) API.

    Constructs the API URL, makes a request, and processes the response.
    If the response status code is 200, the data is cached for future use.

    Returns:
        - List of movie details.
    """
    url = f'{BASE_URL}movie/popular?api_key={TMDB_API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        movies = process_movie_data(data)
        cache.set('cached_movies', movies, timeout=60 * 60 * 12)
        return movies
    else:
        return HttpResponse(
          f"Error fetching data from TMDB API. "
          f"Status code: {response.status_code}",
          status=response.status_code
        )


def process_movie_data(data):
    """
    Processes movie data obtained from The Movie Database (TMDB) API.

    Iterates through the list of movies in the
      'results' key of the provided data.
    For each movie, calls the process_movie_details
      function to extract detailed information.
    Returns a list of processed movie details.

    Parameters:
        - data: Dictionary, data from the TMDB API.

    Returns:
        - List of movie details.
    """
    movies = []

    for movie in data.get('results', []):
        movie_details = process_movie_details(movie)
        movies.append(movie_details)

    return movies


def process_movie_details(movie):
    """
    Processes raw movie data and creates or
      updates a MovieDetails object in the database.

    Extracts information such as movie ID,
      title, poster path, overview, genre IDs,
    genre names (fetched using fetch_genre_names) and release date.
    Uses the extracted data to create or update a
      MovieDetails object in the database.

    Parameters:
        - movie: Dictionary, data for a movie obtained from the TMDB API.

    Returns:
        - None
    """
    movie_id = movie.get('id')
    movie_title = movie.get('title', '')
    movie_poster = movie.get('poster_path', '')
    movie_description = movie.get('overview', '')
    genre_ids = movie.get('genre_ids', [])
    movie_genre = fetch_genre_names(genre_ids)
    movie_release_date = datetime.strptime(
        movie.get('release_date', ''),
        '%Y-%m-%d'
    )

    movie_details, created = MovieDetails.objects.get_or_create(
        movie_id=movie_id,
        defaults={
            'movie_title': movie_title,
            'movie_poster': movie_poster,
            'movie_description': movie_description,
            'movie_genre': movie_genre,
            'movie_release_date': movie_release_date,
        }
    )

    if not created:
        update_existing_movie_details(
            movie_details,
            movie_title,
            movie_poster,
            movie_description,
            movie_genre,
            movie_release_date,
        )

    return movie_details


def update_existing_movie_details(
    movie_details,
    movie_title,
    movie_poster,
    movie_description,
    movie_genre,
    movie_release_date,
):
    """
    Updates the fields of an existing MovieDetails object with new information.

    Modifies the movie title, poster path,
      description, genre and release date.
    of the MovieDetails object. The updated data is then saved to the database.

    Parameters:
        - movie_details: MovieDetails object to be updated.
        - movie_title: Updated title for the movie.
        - movie_poster: Updated poster path for the movie.
        - movie_description: Updated overview/description for the movie.
        - movie_genre: Updated list of genre names for the movie.
        - movie_release_date: Updated release date for the movie.

    Returns:
        - None
    """
    movie_details.movie_title = movie_title
    movie_details.movie_poster = movie_poster
    movie_details.movie_description = movie_description
    movie_details.movie_genre = movie_genre
    movie_details.movie_release_date = movie_release_date
    movie_details.save()


def fetch_genre_names(genre_ids):
    """
    Fetches genre names corresponding to the given list of genre IDs
      from The Movie Database (TMDB) API.

    Constructs the API URL for fetching the list of movie genres.
    Makes a request to the API and extracts genre data.
    Filters the genre names based on the provided genre IDs.

    Parameters:
        - genre_ids: List of integers,
          genre IDs for which names are to be fetched.

    Returns:
        - List of genre names.
    """
    genre_url = f'{BASE_URL}genre/movie/list?api_key={TMDB_API_KEY}'
    response = requests.get(genre_url)

    if response.status_code == 200:
        genres_data = response.json().get('genres', [])
        genre_names = [
            genre['name']
            for genre in genres_data
            if genre['id'] in genre_ids
        ]
        return genre_names

    return []


def movie_detail(request, movie_id):
    """
    Displays details for a specific movie
      and provides the option to add it to a group.

    Retrieves details for the specified movie using its ID.
    Fetches a list of all available groups.
    If the request method is POST, redirects to the add_movie_to_group view.

    Parameters:
        - request: HttpRequest object.
        - movie_id: Integer, ID of the movie to display details for.

    Returns:
        - Rendered HTML page with movie details,
          groups, and an option to add the movie to a group.
    """
    movie = get_object_or_404(MovieDetails, movie_id=movie_id)
    groups = ReviewGroups.objects.all()  # Retrieve all groups

    if request.method == 'POST':
        return add_movie_to_group(request, movie_id)

    return render(
        request,
        'movies/movie_details.html',
        {'movie': movie,
            'groups': groups,
            'back_url': reverse('movies'), 'movie_id': movie_id})


@login_required
def add_movie_to_group(request, movie_id):
    """
    Handles the process of adding a movie to a group.

    If the request method is POST, extracts the group ID from the form data.
    Retrieves the movie and group objects based on the provided IDs.
    Checks if the movie is already in the group.
    If not, adds the movie to the group's list of movies.
    Redirects to the movie details page after the movie has been added to the group.

    Parameters:
        - request: HttpRequest object.
        - movie_id: Integer, ID of the movie to add to a group.

    Returns:
        - HttpResponseRedirect to the movie details page.
    """
    if request.method == 'POST':
        movie = get_object_or_404(MovieDetails, movie_id=movie_id)
        group_id = request.POST.get('group_id')

        group = get_object_or_404(
            ReviewGroups,
            group_id=group_id,
            group_members=request.user
        )

        if movie not in group.group_movies.all():
            group.group_movies.add(movie)

            messages.success(
                request,
                'Movie added to group'
            )
        else:
            messages.info(
                request,
                'The movie is already in the group'
            )

        return HttpResponseRedirect(reverse('movie_details', args=[movie_id]))