from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs/<int:id>/", views.post_detail, name="post_detail"),
]