from rest_framework import routers

from facilities.viewsets import FacilityViewSet

app_name = "facilities"


router = routers.DefaultRouter()
router.register("facilities", FacilityViewSet, "facilities")

urlpatterns = router.urls
