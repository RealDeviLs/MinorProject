from django.db import models
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
# Create your models here.


infra_type_choices = (
    ("lab","lab"),
    ("library","library"),
    ("lecture_hall","lecture hall"),
    ("seminar_hall","seminar hall"),
    ("other","other"),
)

class Infra(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    infra_type = models.CharField(max_length=200,null=True,choices=infra_type_choices)
    department = models.OneToOneField(Site,on_delete= models.CASCADE,related_name="infra",null=True)
    on_site = CurrentSiteManager("department")
    def __str__(self):

        return f"{self.department.name} : {self.title}"

class InfraImage(models.Model):

    image = models.ImageField(upload_to= "infra")
    infra = models.ForeignKey(Infra,on_delete=models.CASCADE,related_name="images")

    def __str__(self):
        return f"{self.infra.department.name} : {self.infra.title} : {self.pk}"
