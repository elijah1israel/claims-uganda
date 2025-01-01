from django.urls import path
from . import views

urlpatterns = [
    path('', views.reminders, name='reminders'),
]