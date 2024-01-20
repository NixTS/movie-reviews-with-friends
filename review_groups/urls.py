from django.urls import path
from review_groups.views import list_of_groups, group_details, create_groups

urlpatterns = [
    path('groups/', list_of_groups, name='list_of_groups'),
    path('groups/<int:group_id>/', group_details, name='group_details'),
    path('groups/create/', create_groups, name='create_groups'),
]