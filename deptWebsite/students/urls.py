from django.urls import path

from .views import (
    add_internship,
    add_placement,
    add_project,
    alumni_page,
    edit_basic_student,
    edit_internship,
    edit_placement,
    edit_project,
    show_for_edit,
)

urlpatterns = [
    path("alumni", alumni_page, name="alumni_page"),
    path("edit/show/<int:batch>", show_for_edit, name="show_for_edit"),
    path("edit/basic/<int:id>", edit_basic_student, name="edit_basic_student"),
    path("edit/add/internship/<int:id>", add_internship, name="add_internship"),
    path("edit/internship/<int:id>", edit_internship, name="edit_internship"),
    path("edit/add/placement/<int:id>", add_placement, name="add_placement"),
    path("edit/placement/<int:id>", edit_placement, name="edit_placement"),
    path("edit/add/project/<int:id>", add_project, name="add_project"),
    path("edit/project/<int:id>", edit_project, name="edit_project"),
]
