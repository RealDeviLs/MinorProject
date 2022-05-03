from django import forms
from django.forms import Textarea

from .models import Infra


class InfraForm(forms.ModelForm):
    class Meta:
        model = Infra
        exclude = ("department", "on_site")
        widgets = {"department_description": Textarea(attrs={"rows": 2})}


# InfraForm = inlineformset_factory(Infra, InfraImage, extra=2,  exclude = ("department", "on_site"))
