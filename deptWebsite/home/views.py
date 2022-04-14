from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
from whitelabel.models import WhiteLabel
from deptWebsite.settings import EMAIL_HOST_USER
def home_page(request):
    print(get_current_site(request))
    print(settings.SITE_ID)
    basic_data = WhiteLabel.on_site.first()
    data = {
        "basic":basic_data
    }
    return render(request,template_name="index.html",context = data)

def contact(request):
    if request.method == 'POST':
        name = request.POST['full-name']
        email =request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        reciever = []
        reciever.append("ra9853044@gmail.com")
        send_mail("New query from  Website ","\n name: "+name+"\n email: "+email+"\n phone: "+phone+"\n message: "+message+ "\n",EMAIL_HOST_USER, reciever)
        messages.success(request,"Your query has been submitted")
        return HttpResponseRedirect(request.path_info)

    return render(request , 'base.html')
