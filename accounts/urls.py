from django.urls import path
from django.contrib.auth import views as auth_views
from .views import list_of_users, user_details, register, edit_own_profile, user_profile

urlpatterns = [
    path('all_users/', list_of_users, name='list_of_users'),
    path('user_details/<int:id>/', user_details, name='user_details'),
    path('user_profile/', user_profile, name='user_profile'),
    path('edit_user_profile/', edit_own_profile, name='edit_own_profile'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),    
]