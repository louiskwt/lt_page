from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("blogs", views.blog_list, name="blogs"),
    path("tag/<slug:tag_slug>/", views.blog_list, name="post_list_by_tag"),
    path("blogs/<int:year>/<int:month>/<int:day>/<slug:post>/", views.post_detail, name="post_detail"),
]