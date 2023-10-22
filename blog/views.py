from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Post


def home(request):
    posts = Post.published.all()
    return render(request, 'home.html', {'post_list': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, published_at__year=year, published_at__month=month, published_at__day=day)

    return render(request, 'post_detail.html', {'post': post})