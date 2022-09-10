from rest_framework import viewsets
from rest_framework_gis import filters

from facilities.models import Facility
from facilities.serializers import FacilitySerializer


class FacilityViewSet(viewsets.ReadOnlyModelViewSet):

    bbox_filter_field = "location"
    filter_backends = (filters.InBBoxFilter,)
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
