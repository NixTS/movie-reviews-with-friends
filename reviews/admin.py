from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_id', 'review_user', 'review_movie', 'review_title', 'review_group'
        )

    search_fields = (
        'review_id', 'review_user', 'review_movie', 'review_title', 'review_group'
        )

    fieldsets = (
        ('Reviews', {
            'fields': ('review_id', 'review_user', 'review_title', 'review_text', 'review_rating', 'review_movie', 'review_group'),
        }),
    )

admin.site.register(Review, ReviewAdmin)
