from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title[:25]

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})