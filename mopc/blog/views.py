from django.shortcuts import render
from .models import Category, Post, Comment

def index(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'blog/index.html', context)

def detail(request, slug):
    post = Post.objects.get(slug=slug)

    context = {
        'post': post
    }

    return render(request, 'blog/detail.html', context)

def category(request, slug):
    category = Category.objects.get(slug=slug)

    context = {
        'category': category
    }

    return render(request, 'blog/category.html', context)