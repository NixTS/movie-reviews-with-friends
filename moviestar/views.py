from django.shortcuts import render
import random


def handler404(request, exception):
    """
    Custom handler for HTTP 404 Not Found errors.

    Displays a user-friendly message on the 404 error page
      with humorous and relatable messages.
    Each time the page is not found, a random message from the list is shown.

    Parameters:
        - request: The Django HTTP request object.
        - exception: The exception that triggered the 404 error.

    Returns:
        - HttpResponse: A rendered HTML response for the 404 error page
          with a random message.
    """
    messages = [
        "To be, or not to be, that is ... well, there is no question... 404!",
        "This page is as elusive as a cat video when you need it. "
        "Try again, hooman!",
        "The cake is a lie. But seriously, the page you're after is missing.",
        "This page is feeling a bit '404 Not Found-ish' today. "
        "It happens to the best of us!",
        "There's no place like home, but it seems this page is lost in Oz. "
        "Click your heels and try again!",
        "This page has gone rogue, just like "
        "Tom Cruise in Mission: Impossible."
        "Try another mission, I mean, link.",
        "Dr. Watson! It seems even Sherlock Holmes couldn't find this page.",
        "Life is like a box of chocolates. "
        "Sometimes you get a 404 error instead.",
        "Here's Johnny! Just kidding, Johnny is not on this page. "
        "Please try another link.",
        "I fear no man. But that thing ... ERROR 404 ... It scares me!"
    ]

    context = {'message': random.choice(messages)}
    return render(request, '404.html', context, status=404)
