from django.urls import path
from .views import infrastructure

urlpatterns = [
    path("", infrastructure,name="infrastructure"),
]
