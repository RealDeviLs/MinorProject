from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class AcademicProgram(models.Model):
    title = models.CharField(max_length=200)
    curriculum = models.FileField(upload_to="curriculum", blank=True, null=True)
    program_outcomes = models.TextField(blank=True)
    peo = HTMLField
    po = HTMLField
    department = models.ForeignKey(
        Site, on_delete=models.CASCADE, related_name="academic_programmes"
    )
    on_site = CurrentSiteManager("department")

    def __str__(self) -> str:
        return f"{self.department.name} : {self.title}"


# class ProgramPeo(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     academic_program = models.ForeignKey(
#         AcademicProgram, on_delete=models.CASCADE, related_name="peo"
#     )

#     def __str__(self):
#         return f"{self.academic_program.title}  {self.title}"
