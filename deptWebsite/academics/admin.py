from django.contrib import admin

from .models import AcademicProgram

# Register your models here.


# class ProgramPeoInline(admin.StackedInline):
#     model = ProgramPeo


@admin.register(AcademicProgram)
class AcademicProgramAdmin(admin.ModelAdmin):
    # inlines = (ProgramPeoInline,)

    class Meta:
        model = AcademicProgram
