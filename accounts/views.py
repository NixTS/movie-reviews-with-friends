from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import CustomUser


def list_of_users(request):
    """
    Lists all users currently in the database.

    Retrieves all user objects from the CustomUser model.
    Prints user information, including ID, username, and user bio.
    Renders the list on the 'accounts/display_users.html' template.

    Note:
        - This function utilizes the CustomUser model, which is a custom extension of the default Django User model.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - Rendered HTML page with a list of all users.
    """
    users = CustomUser.objects.all()
    for user in users:
        print(f"User ID: {id}, Username: {user.username} User Bio: {user.user_bio}")

    return render(request, 'accounts/display_users.html', {'users': users})


def user_details(request, id):
    """
    Displays detailed user information.

    Retrieves details for the specified user using their ID.
    Renders the information on the 'accounts/user_details.html' template.
    Provides a back URL to reverse back to the 'list_of_users' page.

    Parameters:
        - request: HttpRequest object.
        - id: Integer, ID of the user to display details for.

    Returns:
        - Rendered HTML page with detailed user information.
    """
    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'accounts/user_details.html', {'user': user, 'back_url': reverse('list_of_users')})
