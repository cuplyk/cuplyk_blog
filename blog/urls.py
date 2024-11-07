from django.urls import path
from .views import BlogPostListView, BlogPostDetailView, AboutPageView, ContactPageView, ArchivePageView
from . import views

urlpatterns = [
    #path('', PostListView.as_view(), name='home'),
 
    path('', BlogPostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', BlogPostDetailView.as_view(), name='post_detail'),


    path('about/', views.AboutPageView, name='about'),
    path('contacts/', views.ContactPageView, name='contact'),
    path('archive/', views.ArchivePageView, name='archive'),
]