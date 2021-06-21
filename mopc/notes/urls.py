from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllView.as_view(), name='notes'),
    path('category/add/', views.CategoryCreate.as_view(), name='add_category'),
    path('category/<int:pk>/view/', views.CategoryView.as_view(), name='view_category'),
    path('category/<int:pk>/edit/', views.CategoryUpdate.as_view(), name='edit_category'),
    path('category/<int:pk>/delete/', views.CategoryDelete.as_view(), name='delete_category'),
    path('add/', views.NoteCreate.as_view(), name='add_note'),
    path('<int:pk>/edit/', views.NoteUpdate.as_view(), name='edit_note'),
    path('<int:pk>/delete/', views.NoteDelete.as_view(), name='delete_note')
]