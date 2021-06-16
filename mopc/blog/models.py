from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    label = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.label


class Post(models.Model):
    category = models.ManyToManyField(Category, related_name="posts")
    owner = models.ForeignKey(User, related_name='owner_posts', on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField(blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    picture = models.ImageField(upload_to='blog/', null = True, blank = True)

    def __str__(self):
        return self.slug


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete = models.CASCADE)
    owner = models.ForeignKey(User, related_name="owner_comments", on_delete = models.PROTECT)
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.slug