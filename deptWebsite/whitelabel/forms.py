from django import forms
from django.forms import Textarea

from .models import WhiteLabel


class WhiteLabelForm(forms.ModelForm):
    class Meta:
        model = WhiteLabel
        exclude = ("department", "on_site")
        widgets = {"department_description": Textarea(attrs={"cols": 22, "rows": 5})}
