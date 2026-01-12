from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import BlogPost


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ["title", "content", "published"]
    template_name = "blog/blog_create.html"
    success_url = reverse_lazy("blog:blogs_list")


class BlogListView(ListView):
    model = BlogPost
    template_name = "blog/blogs_list.html"
    context_object_name = "blog_posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published=True)


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "blog_post"

    def get_object(self, queryset=None):
        self.blog_post = super().get_object(queryset)
        self.blog_post.count_views += 1
        self.blog_post.save()
        return self.blog_post


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ["title", "content", "published"]
    template_name = "blog/blog_create.html"
    success_url = reverse_lazy("blog:blogs_list")

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = BlogPost
    template_name = "blog/blog_delete.html"
    success_url = reverse_lazy("blog:blogs_list")
