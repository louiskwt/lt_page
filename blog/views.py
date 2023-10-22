from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Post


def home(request):
    posts = Post.published.all()
    return render(request, 'home.html', {'post_list': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)

    return render(request, 'post_detail.html', {'post': post})