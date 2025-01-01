from django.urls import path
from . import views


urlpatterns = [
    path('', views.templates, name='templates'),
    path('upload_template/', views.upload_template, name='upload_template'),
    path('delete_template/<int:template_id>', views.delete_template, name='delete_template'),
]