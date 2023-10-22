from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'published_at', 'status']
    list_filter = ['status', 'created_at', 'published_at']
    search_fields = ['title', 'body']
    raw_id_fields = ['author']
    date_hierarchy = 'published_at'
    ordering = ['status', 'published_at']
