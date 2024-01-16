from django.shortcuts import render
from .models import ReviewGroups


# Create your views here.

def list_of_groups(request):
    groups = ReviewGroups.objects.all()
    for group in groups:
        print(f"Group ID: {group.group_id}, Group Name: {group.group_name}")



    return render(request, 'review_groups/display_groups.html', {'groups': groups})
