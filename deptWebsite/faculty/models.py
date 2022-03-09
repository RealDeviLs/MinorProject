from django.db import models
from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site
from phonenumber_field.modelfields import PhoneNumberField
from students.models import Student
# Create your models here.


class DeptPerson(models.Model):

    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=200)
    qualification = models.TextField()
    address = models.TextField()
    phone = PhoneNumberField(null=True, blank=True)
    email =  models.EmailField()
    research_profile = models.TextField()
    department = models.ForeignKey(Site,on_delete= models.CASCADE,related_name="person")
    on_site = CurrentSiteManager("department")


    def __str__(self) ->str :
        return f"{self.department.name} :{self.name}"

class ResearchInterests(models.Model):
    interest = models.CharField(max_length=200)
    person = models.ForeignKey(DeptPerson,on_delete = models.CASCADE,related_name="interests")

    def __str__(self) -> str :
        return f"{self.person.department.name} : {self.person.name} : {self.interest}"

publication_types = (
    ("book/chapter","book/chapter"),
    ("journal","journal"),
    ("conference","conference"),
)
class Publication(models.Model):
    title = models.TextField()
    description = models.TextField()
    date = models.IntegerField()
    co_authors = models.TextField(null=True)
    publisher = models.CharField(max_length=200)
    citations = models.IntegerField(default=0,null=True) 
    url = models.URLField(null=True,blank=True)
    publication_type = models.CharField(max_length=200, null=True,choices = publication_types)
    person = models.ForeignKey(DeptPerson,on_delete = models.CASCADE,related_name="publicaions")

    def __str__(self) -> str :
        return f"{self.person.department.name} : {self.person.name} : {self.title}"



class Project(models.Model):
    role = models.CharField(max_length=200)
    title = models.CharField(max_length =500)
    description = models.TextField()
    project_type = models.CharField(max_length=200)
    funding_agency = models.CharField(max_length=200)
    date_start = models.DateField(null=True, blank=True,auto_now_add=True)
    date_end = models.DateField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=200)
    co_investigator = models.CharField(max_length=200)
    person = models.ForeignKey(DeptPerson,on_delete = models.CASCADE,related_name="projects")

    def __str__(self) -> str :
        return f"{self.person.department.name} : {self.person.name} : {self.title}"

event_types = (
    ("international","international"),
    ("national","national"),
)

class Event(models.Model):
    category = models.CharField(max_length=200)
    event_type = models.CharField(max_length=200,null=True, choices = event_types)
    title = models.CharField(max_length=500)
    venue = models.CharField(max_length=200)
    date_start = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_end = models.DateTimeField(auto_now=True, blank=True)
    designation = models.CharField(max_length=200)

    person = models.ForeignKey(DeptPerson,on_delete = models.CASCADE,related_name="events")

    def __str__(self) -> str :
        return f"{self.person.department.name} : {self.person.name} : {self.title}"

class Affilation(models.Model):
    designation = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    person = models.ForeignKey(DeptPerson,on_delete = models.CASCADE,related_name="affilations")

    def __str__(self) -> str :
        return f"{self.person.department.name} : {self.person.name} : {self.designation}"


# for PHD and PG make a PHD scholar/PG person first and then link by a FK,

class Scholar(Student):
    research_title = models.CharField(max_length=500)
    research_description = models.TextField()
    faculty = models.ForeignKey(DeptPerson,on_delete=models.CASCADE,related_name="phd_scholars")


class Patent(models.Model):
    title = models.CharField(max_length=200)
    reg_no = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    organization = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    person = models.ForeignKey(DeptPerson,on_delete = models.CASCADE,related_name="patents")

    def __str__(self) -> str :
        return f"{self.person.department.name} : {self.person.name} : {self.title}"


class Responsibility(models.Model):
    position = models.CharField(max_length=200)
    organization = models.CharField(max_length=200)
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    person = models.ForeignKey(DeptPerson,on_delete = models.CASCADE,related_name="responsiblities")

    def __str__(self) -> str :
        return f"{self.person.department.name} : {self.person.name} : {self.title}"

class Award(models.Model):
    title = models.CharField(max_length=200)
    activity = models.CharField(max_length=200)
    given_by = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)

    person = models.ForeignKey(DeptPerson,on_delete = models.CASCADE,related_name="awards")

    def __str__(self) -> str :
        return f"{self.person.department.name} : {self.person.name} : {self.title}"
