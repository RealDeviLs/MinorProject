from django.urls import path

from .views import infra

urlpatterns = [
    path("", infra, name="infra"),
]
