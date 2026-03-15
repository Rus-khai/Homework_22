from django.urls import path
from .views import (
    BlogCreateView,
    BlogListView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
)

app_name = "blog"

urlpatterns = [
    path("blogs/blog_create/", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/", BlogListView.as_view(), name="blogs_list"),
    path("blogs/<int:pk>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blogs/<int:pk>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blogs/<int:pk>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
