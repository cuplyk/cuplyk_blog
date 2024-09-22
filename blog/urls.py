from django.urls import path
from .views import PostListView, PostDetailView, AboutPageView, ContactPageView, ArchivePageView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('about/', views.AboutPageView, name='about'),
    path('contacts/', views.ContactPageView, name='contact'),
    path('archive/', views.ArchivePageView, name='archive'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]