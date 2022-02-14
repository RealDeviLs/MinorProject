from django.urls import path
from .views import activities

urlpatterns = [
    path("", activities,name="activities"),
]
