from django.contrib.gis.db import models as gis_models
from django.utils.translation import gettext_lazy
from django.db import models


class Facility(models.Model):
    name = models.CharField(max_length=200, verbose_name=gettext_lazy("name"))
    address = models.CharField(
        max_length=100, verbose_name=gettext_lazy("address")
    )
    city = models.CharField(max_length=50, verbose_name=gettext_lazy("city"))
    location = gis_models.PointField(
        null=True, blank=True, verbose_name=gettext_lazy("location")
    )

    class Meta:
        verbose_name = gettext_lazy("facility")
        verbose_name_plural = gettext_lazy("facilities")

    def __str__(self):
        return f"{self.name}: {self.city}, {self.address}"
