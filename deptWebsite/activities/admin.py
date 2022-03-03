from django.contrib import admin
from .models import Activity,ActivityImage
# Register your models here.

class ActivityImageInline(admin.StackedInline):
    model = ActivityImage

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = ActivityImageInline,

    class Meta:
        model = Activity


# admin.site.register(ActivityAdmin)