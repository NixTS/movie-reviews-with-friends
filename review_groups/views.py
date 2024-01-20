from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import ReviewGroups
from .forms import ReviewGroupsForm


def list_of_groups(request):
    """
    Renders a list of all review groups available in the database.

    Retrieves all review groups from the database and passes them to the template for rendering.

    Args:
        - request (HttpRequest): The HTTP request object.

    Returns:
        - HttpResponse: Rendered HTML page displaying the list of review groups.

    Template:
        - 'review_groups/display_groups.html'
    """
    groups = ReviewGroups.objects.all()
    for group in groups:
        print(f"Group ID: {group.group_id}, Group Name: {group.group_name}")

    return render(request, 'review_groups/display_groups.html', {'groups': groups})


def group_details(request, group_id):
    """
    Renders the details of a specific group.

    Retrieves the details of a group with the given 'group_id' from the database.
    Renders the group details in the 'review_groups/group_details.html' template.

    Args:
        - request (HttpRequest): The HTTP request object.
        - group_id (int): The unique identifier of the review group.

    Returns:
        - HttpResponse: Rendered HTML page displaying the details of the review group.

    Template:
        - 'review_groups/group_details.html'

    Raises:
        - Http404: If no review group is found with the specified 'group_id'.
    """
    group = get_object_or_404(ReviewGroups, group_id=group_id)

    return render(request, 'review_groups/group_details.html', {'group': group, 'back_url': reverse('list_of_groups')})


def create_groups(request):
    """
    Handles the creation of review groups.

    If the HTTP request method is POST, validates the submitted form data.
    If the form is valid, saves the review group and redirects to the 'list_of_groups' view.
    If the HTTP request method is GET, renders the 'review_groups/create_groups.html' template
    with an empty form for creating a new review group.

    Args:
        - request (HttpRequest): The HTTP request object.

    Returns:
        - HttpResponse: Rendered HTML page displaying the form for creating a review group.

    Template:
        - 'review_groups/create_groups.html'

    Redirects:
        - To the 'list_of_groups' view upon successful creation of a review group.
    """
    if request.method == 'POST':
        form = ReviewGroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_groups')
    else:
        form = ReviewGroupsForm()
        
    return render(request, 'review_groups/create_groups.html', {'form': form})