from django.db import models


class MovieDetails(models.Model):
    """
    Stores movie data retrieved from The Movie Database (TMDB) API.

    Attributes:
        - movie_id (AutoField): Primary key for the movie.
        - movie_title (CharField): Title of the movie.
        - movie_poster (CharField): URL representing the movie poster on TMDB.
        - movie_description (TextField): Description or overview of the movie.
        - movie_genre (JSONField): JSON representation of movie genres.
        - movie_release_date (DateField): Release date of the movie.

    Methods:
        - get_poster_url(): Returns the complete URL for the movie poster.

    Note:
        - The 'movie_poster' field is stored as a URL to save storage space.

    Usage:
        - This model is intended to be used for
          storing and retrieving movie information
        obtained from The Movie Database (TMDB) API.
    """
    movie_id = models.AutoField(primary_key=True)
    movie_title = models.CharField(max_length=255, blank=True, null=True)
    movie_poster = models.CharField(max_length=255, blank=True, null=True)

    def get_poster_url(self):
        if self.movie_poster:
            base_url = 'https://image.tmdb.org/t/p/w300'
            return f'{base_url}{self.movie_poster}'
        return None

    movie_description = models.TextField(
        max_length=10000,
        blank=True,
        null=True
    )
    movie_genre = models.JSONField(blank=True, null=True)
    movie_release_date = models.DateField(blank=True, null=True)
