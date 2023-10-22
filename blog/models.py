from django.db import models
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']
        indexes = [
            models.Index(fields=['-published_at'])
        ]

    def __str__(self):
        return self.title[:25]

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})