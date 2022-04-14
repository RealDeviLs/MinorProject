
from django.urls import path
from .views import alumni_page
urlpatterns = [
        path("alumni", alumni_page,name="alumni_page"),

]
