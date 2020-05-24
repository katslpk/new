from django.views.generic import DetailView
from django.views.generic import ListView

from apps.blog.models import Post


class AllBlogPostsView(ListView):
    template_name = "blog/all_posts.html"
    model = Post


class BlogPostView(DetailView):
    template_name = "blog/post.html"
    model = Post
