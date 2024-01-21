from django.shortcuts import render, redirect
from .forms import ReviewForm

def submit_review(request, group_id, movie_id):
    """
    Handles the submission of user reviews for movies within a review group.

    This view function processes form submissions for user reviews. It validates
    the submitted data using the ReviewForm and, if the form is valid, creates
    a new review associated with the specified movie and review group.

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

            return redirect('movie_review', group_id=group_id, movie_id=movie_id)
    else:
        form = ReviewForm()

    return render(request, 'reviews/review_form.html', {'form': form})