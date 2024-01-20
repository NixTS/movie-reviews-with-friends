from django.urls import path
from .views import list_of_users, user_details, register, edit_own_profile, user_profile

urlpatterns = [
    path('users/', list_of_users, name='list_of_users'),
    path('users/<int:id>/', user_details, name='user_details'),
    path('user_profile/', user_profile, name='user_profile'),
    path('register/', register, name='register'),
    path('edit_user_profile/', edit_own_profile, name='edit_own_profile'),
]