from django.contrib import admin
from .models import NormalizedRecord, AuditLog

admin.site.register(NormalizedRecord)
admin.site.register(AuditLog)
