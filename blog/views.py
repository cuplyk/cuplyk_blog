from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PageVisit

# Create your views here.
#class PostListView(ListView):
 #   model = Post
  #  template_name = 'blog/index.html'
   # context_object_name = 'posts'
    #ordering = ['-created_at']


class BlogPostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']
    paginate_by = 6

class BlogPostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = self.object.tag.all()  # Add tags to context
        return context










def AboutPageView(request):
    my_title = "about page"
    html_template = 'blog/about.html'
    context = {
        'title': my_title,
        'description': 'Learn more about our company and mission.',
    }
    PageVisit.objects.create()
    return render(request, html_template, context)

def ContactPageView(request):
    my_title = "contact page"
    html_template = 'blog/contact.html'
    context = {
        'title': my_title,
        'description': 'Learn more about our company Contacts',
    }
    PageVisit.objects.create()
    return render(request, html_template, context)

def ArchivePageView(request):
    my_title = "archive page"
    html_template = 'blog/archive.html'
    context = {
        'title': my_title,
        'description': 'Learn more about our Archive',
    }
    PageVisit.objects.create()
    return render(request, html_template, context)










class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'