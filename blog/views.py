from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, PageVisit, Tag
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.db.models import Q


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
    
class AllPostsListView(ListView):
    model = Post
    template_name = 'blog/all_posts.html'  # Use a different template if needed
    context_object_name = 'posts'
    ordering = ['-created_at']

    # Remove pagination for this view
    paginate_by = None




def load_more_articles(request):
    page = int(request.GET.get('page', 1))  # Get the page number from the request
    posts_per_page = 6  # Define how many posts per page
    posts = Post.objects.all().order_by('-created_at')  # Order posts as needed
    paginator = Paginator(posts, posts_per_page)

    if page > paginator.num_pages:
        return JsonResponse({'posts': [], 'has_next': False})

    posts_page = paginator.get_page(page)

    # Serialize the post data
    posts_data = [
        {
            'title': post.title,
            'slug': post.slug,
            'author': post.author.username,
            'created_at': post.created_at.strftime('%d %b, %Y'),
            'excerpt': post.content[:100],  # Short snippet of the content
        }
        for post in posts_page.object_list
    ]

    return JsonResponse({
        'posts': posts_data,
        'has_next': posts_page.has_next(),
    })



from django.shortcuts import render
from django.db.models import Q

def search_posts(request):
    query = request.GET.get('q', '').strip()
    results = Post.objects.none()

    if query:
        if query.startswith('#'):
            # Tag-based search
            tag = query[1:]  # Remove the '#' character
            results = Post.objects.filter(tag__name__icontains=tag).distinct()
        else:
            # General text search
            results = Post.objects.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query)
            ).distinct()

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})







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