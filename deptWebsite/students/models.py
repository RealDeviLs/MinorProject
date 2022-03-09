from django.db import models
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
# Create your models here.

course_types = (
    ("btech","btech"),
    ("mtech","mtech"),
    ("phd","phd"),
)
class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    batch = models.IntegerField()
    course = models.CharField(max_length=200,null=True, choices=course_types)
    department = models.ForeignKey(Site,on_delete= models.CASCADE,related_name="students")
    on_site = CurrentSiteManager("department")

    def __str__(self) -> str:
        return f"{self.department.name} : {self.batch} : {self.name}"

intern_types = (
    ("summer","summer"),
    ("six_months","six months")
)
class Internship(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    stipend = models.IntegerField()
    intern_type = models.CharField(max_length=200,null=True, choices = intern_types)
    person = models.ForeignKey(Student,on_delete = models.CASCADE,related_name="internships")
    
    def __str__(self)-> str :
        return f"{self.person.department.name} : {self.person.name} : {self.company}"

offer_types = (
    ("onCampus","onCampus"),
    ("offCampus","offCampus"),
    ("ppo","ppo"),
) 
class Placement(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    ctc = models.IntegerField()
    offer_type = models.CharField(max_length=200,null=True, choices = offer_types)
    person = models.ForeignKey(Student,on_delete = models.CASCADE,related_name="placements")


    def __str__(self)-> str :
        return f"{self.person.department.name} : {self.person.name} : {self.company}"
    
project_types = (
    ("minor","minor"),
    ("major","major"),
)
class Project(models.Model):
    description = models.TextField()
    title  = models.CharField(max_length=500)
    tech = models.CharField(max_length=200)
    remarks = models.TextField()
    project_type = models.CharField(max_length=200,null=True,choices= project_types)
    person = models.ForeignKey(Student,on_delete = models.CASCADE,related_name="projects")

    def __str__(self)-> str :
        return f"{self.person.department.name} : {self.person.name} : {self.company}"