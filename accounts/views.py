from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import CustomUser


# Create your views here.

def list_of_users(request):
    users = CustomUser.objects.all()
    for user in users:
        print(f"User ID: {id}, Username: {user.username} User Bio: {user.user_bio}")

    return render(request, 'accounts/display_users.html', {'users': users})


def user_details(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'accounts/user_details.html', {'user': user, 'back_url': reverse('list_of_users')})
