from django.urls import path
from django.urls import include

from accounts.views import CustomTokenObtainPairView

urlpatterns = [
    path("", include("djoser.urls")),
    path(
        "auth/jwt/create",
        CustomTokenObtainPairView.as_view(),
        name="custom_token_obtain_pair",
    ),
    path("auth/", include("djoser.urls.jwt")),
]
