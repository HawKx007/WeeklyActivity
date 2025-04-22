from django.urls import path
from . import views # Import views from the current directory

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),

  # Map /index/ to the index view
]
