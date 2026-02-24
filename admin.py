from django.contrib import admin

from .models import DataJob

@admin.register(DataJob)
class DataJobAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_type', 'entity_type', 'file_format', 'status', 'created_at']
    search_fields = ['name', 'job_type', 'entity_type', 'file_format']
    readonly_fields = ['created_at', 'updated_at']

