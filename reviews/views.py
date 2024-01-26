from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from .models import Review
from review_groups.models import ReviewGroups
from movies.models import MovieDetails


@login_required
def submit_review(request, group_id, movie_id):
    """
    Handles the submission of user reviews for movies within a review group.

    This view function processes form submissions for user reviews.
    It validates the submitted data using the ReviewForm and,
    if the form is valid, creates a new review associated with the
    specified movie and review group.

    Parameters:
        - request: HttpRequest object.
        - group_id: Integer, ID of the review group.
        - movie_id: Integer, ID of the movie to submit the review for.

    Returns:
        - If the request method is POST and the form is valid, redirects to the
          'movie_review' page for the specified group and movie.
        - If the request method is GET or the form is invalid, renders the
          'review_form.html' template with the ReviewForm.
    """
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.review_user = request.user
            review.review_movie_id = movie_id
            review.review_group_id = group_id
            review.save()

            return redirect(
                'movie_review',
                group_id=group_id,
                movie_id=movie_id
            )
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_form.html', {'form': form})


def get_movie_reviews(group_id, movie_id):
    """
    Fetches and returns reviews for a specific movie within a review group.

    Parameters:
        - group_id: Integer, ID of the review group.
        - movie_id: Integer, ID of the movie.

    Returns:
        - QuerySet of reviews for the specified movie within the review group.
    """
    review_group = get_object_or_404(ReviewGroups, group_id=group_id)
    movie = get_object_or_404(MovieDetails, movie_id=movie_id)

    reviews = Review.objects.filter(
        review_group=review_group,
        review_movie=movie
    )
    return reviews


@login_required
def edit_review(request, group_id, movie_id, review_id):
    """
    Handles the user's request to edit a submitted review.

    Retrieves the specified review using its ID and
      checks if the user is the owner of the review.
    If the request method is POST, processes the submitted form
    to update the review.
    If the form is valid, saves the changes and redirects to the 'movie_review'
      page for the specified group and movie.

    Parameters:
        - request: HttpRequest object.
        - group_id: Integer, ID of the review group associated with the review.
        - movie_id: Integer, ID of the movie associated with the review.
        - review_id: Integer, ID of the review to be edited.

    Returns:
        - If the request method is GET, renders the 'edit_review.html'
          template with the review form.
        - If the request method is POST and the form is valid,
          redirects to the 'movie_review' page.
    """
    review = get_object_or_404(Review, pk=review_id, review_user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(
                'movie_review',
                group_id=group_id,
                movie_id=movie_id
            )
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        'reviews/edit_review.html',
        {'form': form, 'review': review}
    )


@login_required
def delete_review(request, group_id, movie_id, review_id):
    """
    Handles the user's request to delete a review.

    Retrieves the specified review using its ID and checks
    if the user is the owner of the review.
    If the request method is POST, deletes the review and redirects to the
    'movie_review' page for the movie.

    Parameters:
        - request: HttpRequest object.
        - group_id: Integer, ID of the review group associated with the review.
        - movie_id: Integer, ID of the movie associated with the review.
        - review_id: Integer, ID of the review to be deleted.

    Returns:
        - If the request method is GET, renders the 'delete_review.html'
        template with information about the review.
        - If the request method is POST, deletes the review and
        redirects to the 'movie_review' page.
    """
    review = get_object_or_404(Review, pk=review_id, review_user=request.user)

    if request.method == 'POST':
        review.delete()
        return redirect('movie_review', group_id=group_id, movie_id=movie_id)

    return render(request, 'reviews/delete_review.html', {'review': review})
