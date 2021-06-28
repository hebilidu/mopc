from django.contrib import admin
from .models import Tree, Person, Relationship, Event

admin.site.register(Tree)
admin.site.register(Person)
admin.site.register(Relationship)
admin.site.register(Event)