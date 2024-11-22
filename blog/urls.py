from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, AboutPageView, ContactPageView, ArchivePageView, AllPostsListView, load_more_articles
from . import views

urlpatterns = [
    #path('', PostListView.as_view(), name='home'),
 
    path('', BlogPostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('blog/', BlogPostListView.as_view(), name='blog_list'),
    path('blog/all/', AllPostsListView.as_view(), name='all_posts'),

    path('search/', views.search_posts, name='search_posts'),

    path('load-more-articles/', load_more_articles, name='load_more_articles'),

    #path('author/<int:pk>/', views.AuthorPostsView.as_view(), name='author_posts'),


    path('about/', views.AboutPageView, name='about'),
    path('contacts/', views.ContactPageView, name='contact'),
    path('archive/', views.ArchivePageView, name='archive'),
]