from django.urls import path

from .views import add_club, create_dept, edit_club

urlpatterns = [
    path("create-dept", create_dept, name="create_dept"),
    path("add_club", add_club, name="add_club"),
    path("edit_club/<int:id>", edit_club, name="edit_club"),
]
