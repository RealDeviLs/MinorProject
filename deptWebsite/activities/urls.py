from django.urls import path

from .views import activities, activity_detail

urlpatterns = [
    path("", activities, name="activities"),
    path("detail/<int:id>", activity_detail, name="activity_detail"),
]
