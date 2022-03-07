from django.contrib import admin
from .models import Student,Internship,Placement,Project
# Register your models here.

class InternshipInline(admin.StackedInline):
    model = Internship

class PlacementInline(admin.StackedInline):
    model = Placement


class ProjectInline(admin.StackedInline):
    model =  Project


@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    inlines = [InternshipInline,PlacementInline,ProjectInline]

    class Meta:
        model = Student