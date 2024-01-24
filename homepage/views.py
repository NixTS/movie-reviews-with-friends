from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from review_groups.models import ReviewGroups
from accounts.models import CustomUser
import random


def movie_quote(request):
    """
    Displays a random movie quote on the homepage.

    Parameters:
        - request: HttpRequest object.

    Returns:
        - Rendered HTML page for the homepage with a random movie quote.
    """
    movie_quotes = [
        ("Here's looking at you, kid.", "Casablanca (1942)"),
        ("May the Force be with you.", "Star Wars (1977)"),
        ("There's no place like home.", "The Wizard of Oz (1939)"),
        ("I feel the need... the need for speed.", "Top Gun (1986)"),
        ("Keep your friends close, but your enemies closer.", "The Godfather Part II (1974)"),
        ("You can't handle the truth!", "A Few Good Men (1992)"),
        ("Life is like a box of chocolates; you never know what you're gonna get.", "Forrest Gump (1994)"),
        ("To infinity and beyond!", "Toy Story (1995)"),
        ("I'm the king of the world!", "Titanic (1997)"),
        ("Why so serious?", "The Dark Knight (2008)"),
        ("There's no crying in baseball!", "A League of Their Own (1992)"),
        ("I'll be back.", "The Terminator (1984)"),
        ("Here’s Johnny!", "The Shining (1980)"),
        ("Go ahead, make my day.", "Sudden Impact (1983)"),
        ("Houston, we have a problem.", "Apollo 13 (1995)"),
        ("I coulda been a contender.", "On the Waterfront (1954)"),
        ("There are two types of people in the world, my friend: Those with a rope around their neck, and the people who have the job of doing the cutting.", "The Good, the Bad and the Ugly (1966)"),
        ("I see dead people.", "The Sixth Sense (1999)"),
        ("You talking to me?", "Taxi Driver (1976)"),
        ("I'm just a girl, standing in front of a boy, asking him to love her.", "Notting Hill (1999)")
    ]

    selected_message, source = random.choice(movie_quotes)

    return selected_message, source


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

    selected_message, source = movie_quote(request)

    context = {
        'username': request.user.username,
        'user_groups': user_groups,
        'movie_quote': {'message': selected_message, 'source': source},
    }

    return render(request, 'homepage/homepage.html', context)