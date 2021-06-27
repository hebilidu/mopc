
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.text import slugify
from django.views import generic
from .models import Category, Post, Comment
from .forms import CommentForm

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'blog/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.order_by('label')


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'blog/category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'View category'
        return context


class CategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = ['label']
    template_name = 'blog/category.html'
    success_url = reverse_lazy('categories')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Add category'
        return context


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-date_modified')

    
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = [
        'category', 
        'title', 
        'intro', 
        'content',
        'picture'
    ]
    template_name = 'blog/add.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.owner = self.request.user
        post.save()
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    fields = [
        'title',
        'content'
    ]
    template_name = 'blog/detail.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = get_object_or_404(Post, slug = self.kwargs.get("slug"))
        comment.owner = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = get_object_or_404(Post, slug = self.kwargs.get("slug"))
        context['action'] = 'Add comment'
        return context

    def get_success_url(self):
        slug = self.kwargs["slug"]
        return reverse("detail", kwargs={"slug": slug})

