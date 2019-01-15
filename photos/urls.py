from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.DocumentCreateView.as_view(template_name='photos/canvas.html'),
    name='canvas')
]
