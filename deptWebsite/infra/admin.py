from django.contrib import admin
from .models import Infra,InfraImage
# Register your models here.


class InfraImageInline(admin.StackedInline):
    model = InfraImage

@admin.register(Infra)
class InfraAdmin(admin.ModelAdmin):
    inlines = InfraImageInline,

    class Meta:
        model = Infra
