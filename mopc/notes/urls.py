from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/&lt;int:pk&gt;/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/&lt;int:pk&gt;/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/&lt;int:pk&gt;/delete/', PostDeleteView.as_view(), name='post-delete'),
]