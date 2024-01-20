"""
Admin module for managing review groups in the Django admin interface.

This module provides an interface for managing review groups. 
Each group can be created by any user, and movies can be added by users who are members of the respective group.

Attributes:
    - list_display (tuple): Fields displayed in the list view.
    - search_fields (tuple): Fields available for search in the admin interface.
    - fieldsets (tuple): Grouped fields displayed in the group detail view.

Usage:
    - This admin module manages review groups.
    - Users can add movies to groups if they are members of the respective group.
"""

from django.contrib import admin
from .models import ReviewGroups


class ReviewGroupsAdmin(admin.ModelAdmin):
    list_display = (
        'group_id', 'group_name', 'group_creator'
        )

    search_fields = (
        'group_id', 'group_name', 'group_description', 'group_members', 'group_creator'
        )

    fieldsets = (
        ('Group Details', {
            'fields': ('group_name', 'group_creator', 'group_description', 'group_movies', 'group_members'),
        }),
    )

admin.site.register(ReviewGroups, ReviewGroupsAdmin)
