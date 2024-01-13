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