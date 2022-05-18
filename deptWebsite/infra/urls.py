from django.urls import path

from .views import edit_infra, infra, show_infra

urlpatterns = [
    path("", infra, name="infra"),
    path("edit/show", show_infra, name="show_infra_edit"),
    path("edit/<int:id>", edit_infra, name="edit_infra"),
]
