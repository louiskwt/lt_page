from django.urls import path

from .views import BlogDetailView, BlogListView

urlpatterns = [
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    path("", BlogListView.as_view(), name="home")
]