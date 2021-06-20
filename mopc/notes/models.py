from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    label = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})

class Note(models.Model):
    category = models.ForeignKey(Category, on_delete = models.PROTECT, default='undefined')
    title = models.CharField(max_length=255)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='',upload_to='notes/images',blank=True,null=True)
    doc = models.FileField(default='',upload_to='notes/docs',blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('note_detail', kwargs={'pk': self.pk})
