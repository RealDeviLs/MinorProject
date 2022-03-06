from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
# Create your models here.


class WhiteLabel(models.Model):

    department_name = models.CharField(max_length=200)
    department_description = models.CharField(max_length=800)
    vision = models.TextField()
    misison = models.TextField()
    phoneNumber = PhoneNumberField(null = False, blank = False) # Here
    email =  models.EmailField()
    department = models.OneToOneField(Site,on_delete= models.CASCADE,related_name="whitelabel")
    on_site = CurrentSiteManager("department")
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)

    def __str__ (self):
        return self.department_name