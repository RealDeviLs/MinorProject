from django import forms

from .models import Activity, ActivityImage


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        exclude = ("department", "on_site")
        # widgets = {"department_description": Textarea(attrs={ "rows": 5})}


class ActivityImageForm(forms.ModelForm):
    class Meta:
        model = ActivityImage
        exclude = ("activity",)
