from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blogs", views.blog_list, name="blogs"),
    path("blogs/<int:year>/<int:month>/<int:day>/<slug:post>/", views.post_detail, name="post_detail"),
]