from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:case_id>', views.upload_support_document, name='upload_support_document'),
    path('delete/<int:document_id>', views.delete_support_document, name='delete_support_document'),
]