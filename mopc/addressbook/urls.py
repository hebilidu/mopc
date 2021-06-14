from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.index, name="index"),
    path('person_edit/', views.person_edit, name = 'person_edit'),
    path('person_delete/', views.person_delete, name = 'person_delete'),
    path('person_list/', views.person_list, name = 'person_list'),
]