from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def list_of_movies(request):
    return HttpResponse("Hello, Blog!")