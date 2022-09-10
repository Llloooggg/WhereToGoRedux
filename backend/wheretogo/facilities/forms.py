from django import forms
from django.contrib.gis.geos import Point

from facilities.models import Facility


class FacilityLocationForm(forms.ModelForm):

    latitude = forms.FloatField(
        min_value=-90,
        max_value=90,
        required=True,
    )
    longitude = forms.FloatField(
        min_value=-180,
        max_value=180,
        required=True,
    )

    class Meta(object):
        model = Facility
        exclude = []
        widgets = {"location": forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        coordinates = self.initial.get("location", None)
        if coordinates:
            (
                self.initial["longitude"],
                self.initial["latitude"],
            ) = coordinates.tuple

    def clean(self):
        data = super().clean()
        longitude = data.get("longitude")
        latitude = data.get("latitude")
        if latitude and longitude:
            data["location"] = Point(longitude, latitude)
        return data
