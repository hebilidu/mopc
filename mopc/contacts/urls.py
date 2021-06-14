from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_contact/', views.addContact, name='add_contact'),
    path('details/<str:pk>/', views.details, name='details'),
    path('edit_contact/<str:pk>/', views.editContact, name='edit_contact'),
    path('delete_contact/<str:pk>', views.deleteContact, name='delete_contact')
]