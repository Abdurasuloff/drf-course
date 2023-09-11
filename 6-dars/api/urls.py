from django.urls import path
from .views import PostListAPIView, PostDetailAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "api"
urlpatterns = [
    path("", PostListAPIView.as_view(), name="list"),
    path("<int:pk>/", PostDetailAPIView.as_view(), name="detail"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
