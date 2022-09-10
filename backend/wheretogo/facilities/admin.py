from django.contrib import admin

from facilities.models import Facility

from facilities.forms import FacilityLocationForm


class FacilityAdmin(admin.ModelAdmin):
    form = FacilityLocationForm


admin.site.register(Facility, FacilityAdmin)
