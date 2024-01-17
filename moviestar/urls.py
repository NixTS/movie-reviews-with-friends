"""
URL configuration for moviestar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movies.views import list_of_movies, movie_detail
from review_groups.views import list_of_groups, group_details
from accounts.views import list_of_users, user_details

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', list_of_movies, name='movies'),
    path('movies/<int:movie_id>/', movie_detail, name='movie_details'),
    path('groups/', list_of_groups, name='list_of_groups'),
    path('groups/<int:group_id>/', group_details, name='group_details'),
    path('users/', list_of_users, name='list_of_users'),
    path('users/<int:id>/', user_details, name='user_details'),
]