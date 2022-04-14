from django.urls import path

from .views import contact, home_page

urlpatterns = [
    path("", home_page, name="home"),
    path("contact", contact, name="contact"),
]
