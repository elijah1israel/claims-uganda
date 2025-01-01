
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import api

urlpatterns = [
    path('', include('Auth.urls')),
    path('cases/', include('Cases.urls')),
    path('reports/', include('Reports.urls')),
    path('fee-notes/', include('FeeNotes.urls')),
    path('staff/', include('Staff.urls')),
    path('appointments/', include('Appointments.urls')),
    path('pictures/', include('Pictures.urls')),
    path('templates/', include('Templates.urls')),
    path('reminders/', include('Reminders.urls')),
    path('support-documents/', include('SupportDocuments.urls')),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/v1/', api.urls),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

