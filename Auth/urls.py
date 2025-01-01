from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('register_user/<str:token>/', views.register_user, name='register_user'),
    path('send_registration_link/', views.send_registration_link, name='send_registration_link'),
    path('account-settings/', views.account_settings, name='account_settings'),
    path('reset-password/', views.password_reset, name='reset_password'),
    path('reset-password/<str:token>/', views.reset_password, name='reset_password'),
    path('change-password/', views.change_password, name='change_password'),
    path('', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]