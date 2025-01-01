from django.urls import path
from . import views

urlpatterns = [
    path('', views.appointments, name='appointments'),
    path('schedule_appointment/', views.schedule_appointment, name='schedule_appointment'),
    path('delete_all_appointments/', views.delete_all_appointments, name='delete_all_appointments'),
]