from django.contrib import admin

from .models import HeroPhotos, SocietyClub, WhiteLabel

# Register your models here.


class SocietyClubInline(admin.StackedInline):
    model = SocietyClub


@admin.register(WhiteLabel)
class WhiteLabelAdmin(admin.ModelAdmin):
    inlines = (SocietyClubInline,)

    class Meta:
        model = WhiteLabel


admin.site.register(HeroPhotos)
