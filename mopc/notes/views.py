from django.views.generic.base import TemplateView
from .models import Category, Note


class AllView(TemplateView):
    template_name = "notes/triptych.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['notes'] = Note.objects.all()
        context['action'] = 'Display all'
        return context