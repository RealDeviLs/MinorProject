from django.urls import path
from .views import faculty_page

urlpatterns = [
    path("", faculty_page,name="faculty_page"),
]
