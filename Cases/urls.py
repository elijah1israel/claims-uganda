from django.urls import path
from .views import cases, new_case, case_info, comment_case, zip_case_files, delete_case, edit_case, upload_field_notes

urlpatterns = [
    path('', cases, name='cases'),
    path('new_case/', new_case, name='new_case'),
    path('case_info/<int:case_id>', case_info, name='case_info'),
    path('comment_case/<int:case_id>', comment_case, name='comment_case'),
    path('zip_case_files/<int:case_id>', zip_case_files, name='zip_case_files'),
    path('delete_case/<int:case_id>', delete_case, name='delete_case'),
    path('edit_case/<int:case_id>', edit_case, name='edit_case'),
    path('upload_field_notes/<int:case_id>', upload_field_notes, name='upload_field_notes'),
]