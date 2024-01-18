from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import ReviewGroups
from .forms import ReviewGroupsForm


# Create your views here.

def list_of_groups(request):
    groups = ReviewGroups.objects.all()
    for group in groups:
        print(f"Group ID: {group.group_id}, Group Name: {group.group_name}")

    return render(request, 'review_groups/display_groups.html', {'groups': groups})


def group_details(request, group_id):
    group = get_object_or_404(ReviewGroups, group_id=group_id)
    return render(request, 'review_groups/group_details.html', {'group': group, 'back_url': reverse('list_of_groups')})


def create_groups(request):
    if request.method == 'POST':
        form = ReviewGroupsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_groups')
    else:
        form = ReviewGroupsForm()
        
    return render(request, 'review_groups/create_groups.html', {'form': form})