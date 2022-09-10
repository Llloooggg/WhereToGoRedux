from rest_framework_gis import serializers

from facilities.models import Facility


class FacilitySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = Facility
        fields = ("id", "name", "address", "city")
        geo_field = "location"
