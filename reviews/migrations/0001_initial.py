# Generated by Django 4.2.1 on 2024-01-15 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('review_groups', '0003_reviewgroups_group_movies'),
        ('movies', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_id', models.IntegerField(unique=True)),
                ('review_rating', models.IntegerField()),
                ('review_title', models.CharField(max_length=255)),
                ('review_text', models.TextField(blank=True, max_length=20000, null=True)),
                ('review_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_reviews', to='review_groups.reviewgroups')),
                ('review_movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movies.moviedetails')),
                ('review_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('review_user', 'review_movie', 'review_group')},
            },
        ),
    ]