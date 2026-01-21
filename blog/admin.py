from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "preview",
        "created_at",
        "published",
        "count_views",
    )
    list_filter = ("created_at",)
    search_fields = ("title", "published")
