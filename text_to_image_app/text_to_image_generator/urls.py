from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_images, name='generate_images'),
]