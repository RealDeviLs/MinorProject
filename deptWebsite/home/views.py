from academics.models import AcademicProgram
from django.conf import settings
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from students.models import Placement

# Create your views here.
from whitelabel.models import WhiteLabel

from .forms import DeptNewsForm
from .models import DeptNews


def home_page(request):
    print(get_current_site(request))
    print(settings.SITE_ID)
    basic_data = WhiteLabel.on_site.first()
    news = DeptNews.on_site.all()
    programmes = AcademicProgram.on_site.all()
    top_placements = Placement.on_site.all().order_by("ctc")[0:4]
    data = {
        "basic": basic_data,
        "news": news,
        "programmes": programmes,
        "top_placements": top_placements,
    }
    return render(request, template_name="index.html", context=data)


def contact(request):
    if request.method == "POST":
        print("hey hey")
        name = request.POST["full-name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        reciever = []
        reciever.append("atmproject.sem3@gmail.com")
        print(reciever)
        send_mail(
            "New query from  Website ",
            "\n name: "
            + name
            + "\n email: "
            + email
            + "\n phone: "
            + phone
            + "\n message: "
            + message
            + "\n",
            "ra9853044@gmail.com",
            reciever,
        )

        messages.success(request, "Your query has been submitted")
        return HttpResponseRedirect(request.path_info)

    return render(request, "index.html")


def show_news(request):

    site = get_current_site(request)
    if request.method == "POST":
        instance = DeptNews(department=site)
        data = DeptNewsForm(request.POST, request.FILES, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")

        else:
            messages.error(request, f"failed to save, {data.errors}")
    table_data = DeptNews.on_site.all()
    form = DeptNewsForm()
    table_entries = []
    for i in table_data:
        table_entries.append(vars(i))
    data = {"form": form, "table_data": table_entries, "type": "edit_news"}

    return render(request, template_name="showTable.html", context=data)


def edit_news(request, id):

    instance = DeptNews.on_site.filter(id=id).first()
    # id = instance.person.id
    form = DeptNewsForm(instance=instance)

    if request.method == "POST":
        if request.POST.get("delete") == "yes":
            instance.delete()
            return redirect("edit_activity", id)
        data = DeptNewsForm(request.POST, instance=instance)
        if data.is_valid():
            data.save()
            messages.success(request, "Saved")
            return redirect("edit_activity", id)
        else:
            messages.error(request, f"failed to save, {data.errors}")

    data = {"form": form}
    return render(request, template_name="edit_entry.html", context=data)
