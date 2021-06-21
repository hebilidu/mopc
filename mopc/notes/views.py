from django.views.generic.base import TemplateView
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Note


class AllView(TemplateView):
    template_name = "notes/triptych.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['notes'] = Note.objects.all()
        context['action'] = 'Display all'
        return context


class CategoryCreate(LoginRequiredMixin, generic.CreateView):
    model = Category
    fields = '__all__'
    template_name = "notes/triptych.html"
    success_url = reverse_lazy('notes')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['notes'] = Note.objects.all()
        context['action'] = 'Add category'
        return context


class CategoryView(LoginRequiredMixin, TemplateView):
    template_name = "notes/triptych.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk = self.kwargs.get("pk"))
        context['category'] = category
        context['categories'] = Category.objects.all()
        context['notes'] = Note.objects.filter(category = category)
        context['action'] = 'Display category'
        return context

class CategoryUpdate(generic.UpdateView):
    model = Category
    template_name = "notes/triptych.html"


class CategoryDelete(generic.DeleteView):
    model = Category
    template_name = "notes/triptych.html"


class NoteCreate(generic.CreateView):
    model = Note
    fields = ['category', 'title', 'content']
    template_name = "notes/triptych.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['notes'] = Note.objects.all()
        context['action'] = 'Add note'
        return context

    def form_valid(self, form):
        note = form.save(commit=False)
        note.author = self.request.user
        note.save()
        self.id = note.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("edit_note", kwargs={"pk": self.id})


class NoteUpdate(generic.UpdateView):
    model = Note
    fields = ['category', 'title', 'content']
    template_name = "notes/triptych.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['notes'] = Note.objects.all()
        context['note'] = get_object_or_404(Note, pk = self.kwargs.get("pk"))
        context['action'] = 'Edit note'
        return context

    def form_valid(self, form):
        note = form.save(commit=False)
        note.author = self.request.user
        note.save()
        self.id = note.id
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("edit_note", kwargs={"pk": self.id})


class NoteDelete(generic.DeleteView):
    model = Note
    template_name = "notes/triptych.html"
    success_url = reverse_lazy('notes')
    success_message = "Note deleted successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['notes'] = Note.objects.all()
        context['note'] = get_object_or_404(Note, pk = self.kwargs.get("pk"))
        context['action'] = 'Delete note'
        return context