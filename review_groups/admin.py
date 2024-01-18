from django.contrib import admin
from .models import ReviewGroups

# Register your models here.

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
