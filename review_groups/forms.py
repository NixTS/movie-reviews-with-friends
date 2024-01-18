from django import forms
from .models import ReviewGroups

class ReviewGroupsForm(forms.ModelForm):
    class Meta:
        model =ReviewGroups
        fields = ['group_name', 'group_description']