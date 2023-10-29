from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from taggit.models import Tag

from .models import Post


class HomePageView(ListView):
    queryset = Post.published.all()
    context_object_name = 'post_list'
    paginate_by = 3
    template_name = 'home.html'


def blog_list(request, tag_slug=None):
    post_list = Post.published.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
        
    tag_list = [{ 'tag_name': tag.name, 'count': len([p for p in post_list if p.tags.filter(name = tag.name)]) } for tag in Tag.objects.all()]
    paginator = Paginator(post_list, 5)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    

    return render(request, 'blogs.html', {'post_list': posts, 'tag': tag, 'tag_list': tag_list }) 

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, status=Post.Status.PUBLISHED, slug=post, published_at__year=year, published_at__month=month, published_at__day=day)

    return render(request, 'post_detail.html', {'post': post})