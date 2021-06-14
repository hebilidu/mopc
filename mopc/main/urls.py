from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.MainLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('signup/', views.signup, name = 'signup'),
    path('', include('django.contrib.auth.urls')),
    path('', views.main, name='main'),
]