from django.contrib import admin
from .models import MovieDetails

# Register your models here.

class MovieDetailsAdmin(admin.ModelAdmin):
    list_display = (
        'movie_id', 'movie_title', 'display_admin_movie_genre', 'movie_release_date'
        )

    search_fields = (
        'movie_id', 'movie_title', 'movie_genre', 'movie_release_date'
        )

    fieldsets = (
        ('Movie Details', {
            'fields': ('movie_id', 'movie_title', 'movie_genre', 'movie_release_date', 'movie_length', 'movie_description','movie_poster'),
        }),
    )

    def display_admin_movie_genre(self, obj):
        return ', '.join(map(str, obj.movie_genre)) if obj.movie_genre else None


admin.site.register(MovieDetails, MovieDetailsAdmin)
