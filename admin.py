from django.contrib import admin

from .models import DataJob

@admin.register(DataJob)
class DataJobAdmin(admin.ModelAdmin):
    list_display = ['name', 'job_type', 'entity_type', 'file_format', 'status']
    readonly_fields = ['id', 'hub_id', 'created_at', 'updated_at']
    ordering = ['-created_at']

