from django.contrib.gis.db import models
from django.forms.widgets import Textarea
from django.contrib import admin


from facilities.models import Facility


class FacilityAdmin(admin.ModelAdmin):
    formfield_overrides = {models.PointField: {"widget": Textarea}}


admin.site.register(Facility, FacilityAdmin)
