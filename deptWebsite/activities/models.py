from django.db import models
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
# Create your models here.

type_choices  = (
    ("stc","short term course"),
    ("workshop","workshop"),
    ("talk","expert talks"),
    ("contest","contest"),
    ("outreach","outreach"),
    ("other","other"),
)

class Activity(models.Model):
    title = models.CharField(max_length=600)
    domain = models.CharField(max_length=800)
    details = models.TextField()
    date_from = models.DateField()
    date_to = models.DateField(blank=True,null=True)
    cover_Image = models.ImageField(upload_to='activities')
    activity_type = models.CharField(max_length=200,choices=type_choices,null=True)
    department = models.ForeignKey(Site,on_delete= models.CASCADE,related_name="activities",null=True)
    on_site = CurrentSiteManager("department")
    def __str__(self):
        return f"{self.department.name}  {self.title}"


class ActivityImage(models.Model):
    image = models.ImageField(upload_to='activities')
    activity = models.ForeignKey(Activity,on_delete=models.CASCADE,related_name="images")

    def __str__(self):
        return f"{self.activity.department.name} : {self.activity.title} : {self.pk}"