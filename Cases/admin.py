from django.contrib import admin
from .models import Case

admin.site.site_header = 'Claims Management'

admin.site.register(Case)