"""
Admin module for the movies section.

Movies are added through the API from tmdb.com.
This section provides an overview and does not require user interaction.

Attributes:
    - list_display (tuple): Displayed fields in the movie list view.
    - search_fields (tuple): Fields available
      for searching in the admin interface.
    - fieldsets (tuple): Organized groups of fields in the admin form.

Methods:
    - display_admin_movie_genre(obj): Custom method to
      display movie genres in the admin list view.

Usage:
    - This admin module manages movie details
      obtained from The Movie Database (TMDB) API.
    - Movies are added automatically through the API,
      and this interface offers an overview.
"""
from django.contrib import admin
from .models import MovieDetails


class MovieDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'movie_id',
        'movie_title',
        'display_admin_movie_genre',
        'movie_release_date'
        )

    search_fields = (
        'movie_id',
        'movie_title',
        'movie_genre',
        'movie_release_date'
        )

    fieldsets = (
        ('Movie Details', {
            'fields': ('movie_id',
                       'movie_title',
                       'movie_genre',
                       'movie_release_date',
                       'movie_duration',
                       'movie_description',
                       'movie_poster'),
        }),
    )

    def display_admin_movie_genre(self, obj):
        """
        Display function for rendering movie genres.

        Returns:
            - str or None: Comma-separated string of
              movie genres if available, otherwise None.

        Usage:
            - This function is used to customize the display of movie genres
              in the Django admin interface
            for the MovieDetails model. It joins the genre names
              into a single string, separated by commas.
            - If no genres are available, it returns None.
        """
        return ', '.join(map(str, obj.movie_genre)) \
            if obj.movie_genre else None


admin.site.register(MovieDetails, MovieDetailsAdmin)
