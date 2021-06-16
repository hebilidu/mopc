from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog'),
    path('addpost/', views.PostCreateView.as_view(), name='addpost'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('<str:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('category/add/', views.CategoryCreateView.as_view(), name='addcategory'),
    path('category/<str:slug>/', views.CategoryDetailView.as_view(), name='category'),
    path('<str:slug>/comment/add/', views.CommentCreateView.as_view(), name='addcomment'),
]