from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from photologue.models import Gallery, Photo

class GalleryCreate(LoginRequiredMixin, generic.CreateView):
    model = Gallery
    fields = '__all__'
    template_name = 'photo/galleryadd.html'
    success_url = reverse_lazy('photologue:gallery-list')


class GalleryDetail(LoginRequiredMixin, generic.DetailView):
    model = Gallery
    template_name = 'photo/gallerydetail.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'View category'
        return context

class GalleryUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Gallery
    fields = '__all__'
    template_name = 'photo/gallerydetail.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Edit category'
        return context


class GalleryDelete(LoginRequiredMixin, generic.DeleteView):
    pass


class PhotoCreate(LoginRequiredMixin, generic.CreateView):
    model = Photo
    fields = '__all__'
    template_name = 'photo/photo.html'
    success_url = reverse_lazy('photologue:gallery-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Add photo'
        return context


class PhotoUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Photo
    fields = '__all__'
    template_name = 'photo/photo.html'
    success_url = reverse_lazy('photologue:gallery-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Edit photo'
        return context


class PhotoDelete(LoginRequiredMixin, generic.DeleteView):
    pass