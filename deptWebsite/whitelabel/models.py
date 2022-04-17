from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models

# Create your models here.
from faculty.models import DeptPerson
from phonenumber_field.modelfields import PhoneNumberField


class WhiteLabel(models.Model):

    department_name = models.CharField(max_length=200)
    department_description = models.CharField(max_length=800)
    vision = models.TextField()
    misison = models.TextField()
    phoneNumber = PhoneNumberField(null=False, blank=False)  # Here
    email = models.EmailField()
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    hod = models.ForeignKey(DeptPerson, on_delete=models.CASCADE, null=True)
    hod_message = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="HeroPhotos", null=True, blank=True)
    department = models.ForeignKey(
        Site, on_delete=models.CASCADE, related_name="whitelabel", null=True
    )
    on_site = CurrentSiteManager("department")

    def __str__(self):
        return self.department_name


class SocietyClub(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    site = models.URLField(null=True, blank=True)
    dept = models.ForeignKey(WhiteLabel, on_delete=models.CASCADE, related_name="clubs")

    def __str__(self) -> str:
        return f"{self.dept.department.name} : {self.title}"


class HeroPhotos(models.Model):
    image = models.ImageField(upload_to="HeroPhotos")

    dept = models.ForeignKey(
        WhiteLabel, on_delete=models.CASCADE, related_name="photos"
    )

    def __str__(self):
        return f"{self.department.title} {self.pk}"
