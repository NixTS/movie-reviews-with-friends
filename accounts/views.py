from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from .forms import RegistrationForm, UserProfileEditForm


def list_of_users(request):
    """
    Lists all users currently in the database.

    Retrieves all user objects from the CustomUser model.
    Prints user information, including ID, username, and user bio.
    Renders the list on the 'accounts/display_users.html' template.

    Note:
        - This function utilizes the CustomUser model,
        which is a custom extension of the default Django User model.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - Rendered HTML page with a list of all users.
    """
    users = CustomUser.objects.all()

    return render(request, 'accounts/display_users.html', {'users': users})


@login_required
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
    return render(
        request,
        'accounts/user_details.html',
        {'user': user, 'back_url': reverse('list_of_users')}
    )


def register(request):
    """
    View for user registration.

    Handles both GET and POST requests. If the request is a POST request,
    it validates the registration form.
    If the form is valid, it creates a new user,
    logs in the user, and redirects to the movies page. If the request is a GET
    request, displays the registration form.

    Args:
        - request: The HTTP object.

    Returns:
        - If the request is a POST request and the form is valid:
        Redirects to the movies page after creating and logging in the user.
        - If the request is a GET request or the form is invalid:
        Renders the registration form page with the form.
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            messages.success(
                request,
                'Successfully registered for an account'
            )

            return redirect('homepage')
    else:
        form = RegistrationForm()


    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_own_profile(request):
    """
    Displays and allows the logged-in user to update their user profile.

    Handles the GET request to display the user profile form.
    Handles the POST request to update the user profile
    when the form is submitted.

    Template: 'accounts/edit_own_profile.html'
    """
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            messages.success(
                    request,
                    'Profile updated'
                )
            
            return redirect('user_profile')
    else:
        form = UserProfileEditForm(instance=request.user)

    return render(request, 'profiles/edit_own_profile.html', {'form': form})


@login_required
def user_profile(request):
    """
    Displays the user's own profile information.

    Template: 'profile/user_profile.html'
    """
    user = request.user
    return render(request, 'profiles/user_profile.html', {'user': user})
