"""
Admin module for managing user reviews.

This admin module provides an interface for handling reviews submitted by users.
It includes fields such as review ID, user, movie, title, and group.

Attributes:
    - list_display (tuple): The fields to be displayed in the list view.
    - search_fields (tuple): Fields that can be searched in the admin interface.
    - fieldsets (tuple): Defines the structure and grouping of fields in the admin interface.

Usage:
    - This admin module manages user reviews.
"""

from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_id', 'review_user', 'review_movie', 'review_title', 'review_group'
        )

    search_fields = (
        'review_user', 'review_movie', 'review_title', 'review_group'
        )

    fieldsets = (
        ('Reviews', {
            'fields': ('review_user', 'review_title', 'review_text', 'review_rating', 'review_movie', 'review_group'),
        }),
    )

admin.site.register(Review, ReviewAdmin)
