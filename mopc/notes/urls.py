from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllView.as_view(), name='notes'),
]