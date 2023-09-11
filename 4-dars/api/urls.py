from django.urls import path
from .views import PostListAPIView, PostDetailAPIView

app_name = "api"
urlpatterns = [
    path("", PostListAPIView.as_view(), name="list"),
    path("<int:pk>/", PostDetailAPIView.as_view(), name="detail"),
]
