from django.urls import path

from .views import edit_basic, faculty_detail, faculty_page

urlpatterns = [
    path("", faculty_page, name="faculty_page"),
    path("profile/<int:id>", faculty_detail, name="profile"),
    path("edit/basic/<int:id>", edit_basic, name="edit_basic_faculty"),
]
