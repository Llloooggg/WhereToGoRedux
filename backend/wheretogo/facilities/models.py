from django.contrib.gis.db import models as gis_models
from django.utils.translation import gettext_lazy as _
from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("name"))
    address = models.CharField(max_length=100, verbose_name=_("address"))
    city = models.CharField(max_length=50, verbose_name=_("city"))
    location = gis_models.PointField(
        null=True, blank=True, verbose_name=_("location")
    )

    class Meta:
        verbose_name = _("facility")
        verbose_name_plural = _("facilities")

    def __str__(self):
        return f"{self.name}: {self.city}, {self.address}"
