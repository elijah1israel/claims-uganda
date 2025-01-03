from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_notifications, name='notifications'),
]