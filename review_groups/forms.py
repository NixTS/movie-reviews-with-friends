from django import forms
from .models import ReviewGroups

class ReviewGroupsForm(forms.ModelForm):
    """
    Form for creating or updating a review group.

    This form is based on the ReviewGroups model and includes fields for group_name and group_description.

    Attributes:
        - model: The associated ReviewGroups model.
        - fields: The fields to be included in the form.
    """
    class Meta:
        model =ReviewGroups
        fields = ['group_name', 'group_description']