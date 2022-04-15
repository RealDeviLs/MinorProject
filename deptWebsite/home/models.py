from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models

# Create your models here.


class DeptNews(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    date_end = models.DateField(null=True, blank=True)
    files = models.FileField(null=True, blank=True, upload_to="newsMedia")
    department = models.OneToOneField(
        Site, on_delete=models.CASCADE, related_name="news"
    )
    on_site = CurrentSiteManager("department")

    def __str__(self):
        return self.title
