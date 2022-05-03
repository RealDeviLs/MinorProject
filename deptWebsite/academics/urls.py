from django.urls import path

from .views import edit_academic_program, show_academic_programs

urlpatterns = [
    path("edit/show", show_academic_programs, name="show_activities"),
    path("edit/<int:id>", edit_academic_program, name="edit_activity"),
]
