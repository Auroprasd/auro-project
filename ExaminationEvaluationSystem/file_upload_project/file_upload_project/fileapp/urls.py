# fileapp/urls.py
from django.urls import path
from . import views  # Import views from fileapp

urlpatterns = [
    path('', views.file_list, name='file_list'),  # Define your routes here
    path('upload/', views.upload_file, name='upload_file'),
    path('file/<int:pk>/', views.file_detail, name='file_detail'),
    path('file/<int:pk>/update/', views.update_file, name='update_file'),
]

