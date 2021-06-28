from django.urls import path
from . import views

urlpatterns = [
    path('tree/list/', views.TreeList.as_view(), name='treelist'),
    path('tree/add/', views.TreeCreate.as_view(), name='treeadd'),
    path('tree/<int:pk>/', views.TreeDetail.as_view(), name='treedetail'),
    path('tree/<int:pk>/edit/', views.TreeUpdate.as_view(), name='treeedit'),
    path('person/list/', views.PersonList.as_view(), name='personlist'),
    path('person/add/', views.PersonCreate.as_view(), name='personadd'),
    path('person/<int:pk>/', views.PersonDetail.as_view(), name='persondetail'),
    path('person/<int:pk>/edit/', views.PersonUpdate.as_view(), name='personedit'),
    path('person/<int:pk>/delete/', views.PersonDelete.as_view(), name='persondelete'),
]