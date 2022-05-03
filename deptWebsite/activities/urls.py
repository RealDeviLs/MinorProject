from django.urls import path

from .views import activities, activity_detail, edit_activity, show_activities

urlpatterns = [
    path("", activities, name="activities"),
    path("detail/<int:id>", activity_detail, name="activity_detail"),
    path("edit/show", show_activities, name="show_activities"),
    path("edit/<int:id>", edit_activity, name="edit_activity"),
]
