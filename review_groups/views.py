from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import ReviewGroups
from movies.models import MovieDetails
from .forms import ReviewGroupsForm
from reviews.forms import ReviewForm
from reviews.views import get_movie_reviews


def list_of_groups(request):
    """
    Renders a list of all review groups available in the database.

    Retrieves all review groups from the database
      and passes them to the template for rendering.

    Args:
        - request (HttpRequest): The HTTP request object.

    Returns:
        - HttpResponse: Rendered HTML page
          displaying the list of review groups.

    Template:
        - 'review_groups/display_groups.html'
    """
    groups = ReviewGroups.objects.all()

    return render(
        request,
        'review_groups/display_groups.html',
        {'groups': groups}
    )


def group_details(request, group_id):
    """
    Renders the details of a specific group.

    Retrieves the details of a group
      with the given 'group_id' from the database.
    Renders the group details in the
      'review_groups/group_details.html' template.

    Args:
        - request (HttpRequest): The HTTP request object.
        - group_id (int): The unique identifier of the review group.

    Returns:
        - HttpResponse: Rendered HTML page
          displaying the details of the review group.

    Template:
        - 'review_groups/group_details.html'

    Raises:
        - Http404: If no review group is found with the specified 'group_id'.
    """
    group = get_object_or_404(ReviewGroups, group_id=group_id)

    return render(
        request,
        'review_groups/group_details.html',
        {'group': group, 'back_url': reverse('list_of_groups')}
    )


@login_required
def create_groups(request):
    """
    Handles the creation of review groups.

    If the HTTP request method is POST, validates the submitted form data.
    If the form is valid, saves the review group and
      redirects to the 'list_of_groups' view.
    If the HTTP request method is GET, renders the
      'review_groups/create_groups.html' template
    with an empty form for creating a new review group.

    Args:
        - request (HttpRequest): The HTTP request object.

    Returns:
        - HttpResponse: Rendered HTML page displaying
          the form for creating a review group.

    Template:
        - 'review_groups/create_groups.html'

    Redirects:
        - To the 'list_of_groups' view upon
          successful creation of a review group.
    """
    if request.method == 'POST':
        form = ReviewGroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_groups')
    else:
        form = ReviewGroupsForm()

    return render(
        request,
        'review_groups/create_groups.html',
        {'form': form, 'back_url': reverse('list_of_groups')}
    )


@login_required
def edit_group(request, group_id):
    """
    Handles the editing of review groups.

    If the form is valid, saves the review group and
      redirects to the 'group_details' view.
    If the HTTP request method is GET,
      renders the 'review_groups/edit_group.html' template
    with the form pre-filled with the current group details for editing.
    If the HTTP request method is POST, validates the submitted form data.

    Args:
        - request (HttpRequest): The HTTP request object.

    Returns:
        - HttpResponse:
          Rendered HTML page displaying the form for editing a review group.

    Template:
        - 'review_groups/edit_group.html'

    Redirects:
        - To the 'group_details' view upon successful editing
          of a review group.
    """
    group = get_object_or_404(ReviewGroups, group_id=group_id)

    if request.user == group.group_creator:
        if request.method == 'POST':
            form = ReviewGroupsForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                return redirect('group_details', group_id=group_id)
        else:
            form = ReviewGroupsForm(instance=group)

        return render(
            request,
            'review_groups/edit_group.html',
            {'form': form, 'group': group}
        )
    else:
        return redirect('access_denied')


@login_required
def delete_group(request, group_id):
    """
    Handles the deletion of review groups.

    If the HTTP request method is GET and the logged-in user
      is the creator of the group,
    renders the 'review_groups/delete_group.html'
      template to confirm the deletion.
    If the HTTP request method is POST and the logged-in user
      is the creator of the group,
    deletes the review group and redirects to the 'list_of_groups' view.

    Args:
        - request (HttpRequest): The HTTP request object.
        - group_id (int): The ID of the group to be deleted.

    Returns:
        - HttpResponse: Rendered HTML page for confirming
          the deletion of a review group.

    Template:
        - 'review_groups/delete_group.html'

    Redirects:
        - To the 'list_of_groups' view upon successful deletion
          of a review group.
    """
    group = get_object_or_404(ReviewGroups, group_id=group_id)

    if request.user == group.group_creator:
        if request.method == 'POST':
            group.delete()
            return redirect('list_of_groups')

        return render(
            request,
            'review_groups/delete_group.html',
            {'group': group}
        )
    else:
        return render(request, 'review_groups/access_denied.html')


def movie_review(request, group_id, movie_id):
    """
    Displays details for a specific movie within a review group.

    Retrieves details for the specified movie using its ID.
    Fetches a list of all available review groups.

    Parameters:
        - request: HttpRequest object.
        - group_id: Integer, ID of the review group.
        - movie_id: Integer, ID of the movie to display details for.

    Returns:
        - Rendered HTML page with movie details
          within the context of a review group.
    """
    group = get_object_or_404(ReviewGroups, group_id=group_id)

    if request.user in group.group_members.all():
        review_group = get_object_or_404(ReviewGroups, group_id=group_id)
        movie = get_object_or_404(MovieDetails, movie_id=movie_id)
        group_name = review_group.group_name

        reviews = get_movie_reviews(group_id, movie_id)

        back_url = reverse('group_details', kwargs={'group_id': group_id})

        context = {
            'group': review_group,
            'movie': movie,
            'group_name': group_name,
            'reviews': reviews,
            'back_url': back_url,
            'form': ReviewForm(),
        }

        return render(request, 'review_groups/movie_review_in_group.html', context)
    else:
        return redirect('access_denied')


@login_required
def join_leave_group(request, group_id):
    """
    Handles the user's request to join or leave a review group.

    Retrieves the specified review group using its ID.
    Checks if the requesting user is already a member of the group.
    If the user is a member, removes them from the group;
      otherwise, adds them to the group.

    Parameters:
        - request: HttpRequest object.
        - group_id: Integer, ID of the review group to join or leave.

    Returns:
        - Redirects to the 'group_details' page for the
          specified review group after the join/leave action.
    """
    group = ReviewGroups.objects.get(pk=group_id)

    if request.user in group.group_members.all():
        group.group_members.remove(request.user)
    else:
        group.group_members.add(request.user)

    return redirect('group_details', group_id=group_id)
