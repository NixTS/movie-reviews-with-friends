"""
Admin module for managing custom user models in the Django admin interface.

This module extends the default UserAdmin provided by Django
to include additional fields such as date of birth and a biography.

Attributes:
    - list_display (tuple): Fields displayed in the list view.
    - fieldsets (tuple): Grouped fields displayed in the user detail view.
    - add_fieldsets (tuple): Fields displayed in the add user view.

Usage:
    - This admin module manages user information.
    - Including personal and profile details, permissions, and important dates.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Profile info', {
            'fields': ('user_date_of_birth', 'user_bio')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Profile info', {
            'fields': ('user_date_of_birth', 'user_bio')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
