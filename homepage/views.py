from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from review_groups.models import ReviewGroups
from accounts.models import CustomUser

@login_required
def homepage(request):
    """
    Renders the homepage with user-specific content.

    If the user is not logged in, redirects to the login page.
    Retrieves the user's username and groups.
    Passes the data to the 'homepage.html' template for rendering.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - Rendered HTML page for the homepage or a redirect to the login page.
    """
    user_groups = ReviewGroups.objects.filter(group_members=request.user)

    context = {
        'username': request.user.username,
        'user_groups': user_groups,
    }

    return render(request, 'homepage/homepage.html', context)