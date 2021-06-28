from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Tree, Person, Relationship, Event


class Cell():
    """A family cell includes a couple and its children. Built from the 'P' Relationship instances"""
    def __init__(self, relationship):
        # self.parent_1 = relationship.a
        # self.parent_2 = relationship.b
        pass


class TreeList(LoginRequiredMixin, generic.ListView):
    model = Tree
    template_name = 'genealogy/treelist.html'
    context_object_name = 'trees'

    def get_queryset(self):
        return Tree.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'List trees'
        return context    


class TreeDetail(LoginRequiredMixin, generic.DetailView):
    model = Tree
    template_name = 'genealogy/treedetail.html'
    context_object_name = 'tree'

    def get_object(self):
        return get_object_or_404(Tree, id = self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'View tree'
        return context

    # def calc_depth(self):
    #     """Go through Relationship instances with parent-child type"""
    #     relationships = Relationship.objects.filter(tree=self, type='P')
    #     # Look for longest parent-child chain
    #     count = 0
    #     for r in relationships:
    #         parent = r.a
    #         upper = Relationship.objects.filter
    #         while True:
    #             count += 1


class TreeCreate(LoginRequiredMixin, generic.CreateView):
    model = Tree
    fields = ['name']
    template_name = 'genealogy/treedetail.html'
    context_object_name = 'tree'
    success_url = reverse_lazy('treelist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create tree'
        return context

    def form_valid(self, form):
        tree = form.save(commit=False)
        tree.owner = self.request.user
        tree.save()
        return super().form_valid(form)


class TreeUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Tree
    fields = ['name']
    template_name = 'genealogy/treedetail.html'
    context_object_name = 'tree'
    success_url = reverse_lazy('treelist')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Edit tree'
        return context

    def form_valid(self, form):
        tree = form.save(commit=False)
        tree.owner = self.request.user
        tree.save()
        return super().form_valid(form)


class PersonList(LoginRequiredMixin, generic.ListView):
    model = Person
    template_name = 'genealogy/personlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tree = Tree.objects.filter(id=self.kwargs.get("pk"))
        context['tree'] = tree
        context['relationships'] = Relationship.objects.filter(tree = tree)
        context['action'] = 'List persons'
        return context


class PersonCreate(LoginRequiredMixin, generic.CreateView):
    model = Person
    fields = '__all__'
    template_name = 'genealogy/persondetail.html'
    success_message = "Person created successfully"
    success_url = reverse_lazy('personlist')


class PersonDetail(LoginRequiredMixin, generic.DetailView):
    model = Person
    template_name = 'genealogy/persondetail.html'


class PersonUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Person
    fields = '__all__'
    template_name = 'genealogy/persondetail.html'
    success_url = reverse_lazy('personlist')

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Person, id = id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Update Person'
        return context

class PersonDelete(LoginRequiredMixin, generic.DeleteView):
    model = Person
    fields = '__all__'
    template_name = 'genealogy/persondetail.html'
    success_url = reverse_lazy('personlist')
    success_message = "Person deleted successfully"

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(Person, id = id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Delete Person'
        return context 