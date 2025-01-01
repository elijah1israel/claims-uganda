from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:case_id>/', views.upload_report, name='upload_report'),
    path('', views.reports, name='reports'),
    path('download/<int:report_id>/', views.download_report, name='download_report'),
    path('delete/<int:report_id>/', views.delete_report, name='delete_report'),
    path('info/<int:report_id>/', views.report_info, name='report_info'),
    path('submit/<int:report_id>/', views.submit_report, name='submit_report'),
]