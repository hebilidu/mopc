from django.urls import path
from . import views

urlpatterns = [
    path('gallery/add/', views.GalleryCreate.as_view(), name='galleryadd'),
    path('gallery/<int:pk>/', views.GalleryDetail.as_view(), name='gallerydetail'),
    path('gallery/<int:pk>/edit/', views.GalleryUpdate.as_view(), name='galleryedit'),
    path('gallery/<int:pk>/delete/', views.GalleryDelete.as_view(), name='gallerydelete'),
    path('add/', views.PhotoCreate.as_view(), name='photoadd'),
    path('<int:pk>/edit/', views.PhotoUpdate.as_view(), name='photoedit'),
    path('<int:pk>/delete/', views.PhotoDelete.as_view(), name='photodelete'),
]