from django.urls import path

from .views import contact, edit_news, home_page, show_news

urlpatterns = [
    path("", home_page, name="home"),
    path("contact", contact, name="contact"),
    path("show/news", show_news, name="show_news"),
    path("show/news/edit_news/<int:id>", edit_news, name="edit_news"),
]
