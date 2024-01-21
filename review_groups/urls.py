from django.urls import path
from review_groups.views import list_of_groups, group_details, create_groups, edit_group, delete_group

urlpatterns = [
    path('list_groups/', list_of_groups, name='list_of_groups'),
    path('details/<int:group_id>/', group_details, name='group_details'),
    path('create/', create_groups, name='create_groups'),
    path('<int:group_id>/edit/', edit_group, name='edit_group'),
    path('<int:group_id>/delete/', delete_group, name='delete_group'),
]