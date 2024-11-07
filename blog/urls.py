from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, AboutPageView, ContactPageView, ArchivePageView
from . import views

urlpatterns = [
    #path('', PostListView.as_view(), name='home'),
 
    path('', BlogPostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/', views.BlogPostDetailView.as_view(), name='post_detail'),
    #path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),  # Tag-specific posts
    #path('author/<int:pk>/', views.AuthorPostsView.as_view(), name='author_posts'),


    path('about/', views.AboutPageView, name='about'),
    path('contacts/', views.ContactPageView, name='contact'),
    path('archive/', views.ArchivePageView, name='archive'),
]