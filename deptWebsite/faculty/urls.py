from django.urls import path

from .views import faculty_detail, faculty_page

urlpatterns = [
    path("", faculty_page, name="faculty_page"),
    path("profile/<int:id>", faculty_detail, name="profile"),
]
