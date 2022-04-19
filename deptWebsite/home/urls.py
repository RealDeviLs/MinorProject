from django.urls import path

from .views import contact, home_page, show_news

urlpatterns = [
    path("", home_page, name="home"),
    path("contact", contact, name="contact"),
    path("show/news", show_news, name="show_news"),
]
