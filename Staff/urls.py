from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff, name='staff'),
    path('make_staff_inactive/<int:pk>/', views.make_staff_inactive, name='make_staff_inactive'),
    path('make_staff_active/<int:pk>/', views.make_staff_active, name='make_staff_active'),
    path('staff_profile/<int:pk>/', views.staff_profile, name='staff_profile'),
    path('upload_profile_picture/', views.upload_profile_picture, name='upload_profile_picture'),
    path('delete_profile_picture/', views.delete_profile_picture, name='delete_profile_picture'),
    path('change_department/<int:staff_id>/', views.change_department, name='change_department'),
    path('edit_profile/<int:pk>/', views.edit_profile, name='edit_profile'),
]