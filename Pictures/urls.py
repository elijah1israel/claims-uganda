from django.urls import path
from . import views

urlpatterns = [
    path('upload_picture/<int:case_id>', views.upload_picture, name='upload_picture'),
    path('delete_picture/<int:picture_id>', views.delete_picture, name='delete_picture'),
]