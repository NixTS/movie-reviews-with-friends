from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),

]