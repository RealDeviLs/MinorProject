from django.urls import path

from .views import create_dept

urlpatterns = [
    path("create-dept", create_dept, name="create_dept"),
]
