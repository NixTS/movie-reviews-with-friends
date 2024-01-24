from django.urls import path
from django.contrib.auth.decorators import login_required
from review_groups.views import list_of_groups, group_details, create_groups, edit_group, delete_group, movie_review, join_leave_group

urlpatterns = [
    path('list_groups/', list_of_groups, name='list_of_groups'),
    path('details/<int:group_id>/', group_details, name='group_details'),
    path('create/', login_required(create_groups), name='create_groups'),
    path('<int:group_id>/edit/', login_required(edit_group), name='edit_group'),
    path('<int:group_id>/delete/', login_required(delete_group), name='delete_group'),
    path('<int:group_id>/<int:movie_id>/reviews', movie_review, name='movie_review'),
    path('<int:group_id>/join_leave/', login_required(join_leave_group), name='join_leave_group'),
]