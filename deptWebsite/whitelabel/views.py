from django.shortcuts import render

from .forms import WhiteLabelForm

# Create your views here.


def create_dept(request):

    white_label_form = WhiteLabelForm

    data = {
        "white_label_form": white_label_form,
    }
    return render(request, template_name="create_dept.html", context=data)
