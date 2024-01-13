from django.db import models

# Create your models here.

class MovieDetails(models.Model):
    movie_id = models.IntegerField(unique=True)
    movie_title = models.CharField(max_length=255, blank=True, null=True)
    movie_poster = models.CharField(max_length=255, blank=True, null=True)
    
    def get_poster_url(self):
        if self.movie_poster:
            base_url = 'https://image.tmdb.org/t/p/w300'
            return f'{base_url}{self.movie_poster}'
        return None

    movie_description = models.TextField(max_length=10000, blank=True, null=True)
    movie_genre = models.JSONField(blank=True, null=True)
    movie_release_date = models.DateField(blank=True, null=True)
    movie_length = models.DurationField(blank=True, null=True)