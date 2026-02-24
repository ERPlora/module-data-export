from django import forms
from django.utils.translation import gettext_lazy as _

from .models import DataJob

class DataJobForm(forms.ModelForm):
    class Meta:
        model = DataJob
        fields = ['name', 'job_type', 'entity_type', 'file_format', 'status', 'records_count', 'file_path', 'error_message', 'completed_at']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'job_type': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'entity_type': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'file_format': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'status': forms.Select(attrs={'class': 'select select-sm w-full'}),
            'records_count': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'number'}),
            'file_path': forms.TextInput(attrs={'class': 'input input-sm w-full'}),
            'error_message': forms.Textarea(attrs={'class': 'textarea textarea-sm w-full', 'rows': 3}),
            'completed_at': forms.TextInput(attrs={'class': 'input input-sm w-full', 'type': 'datetime-local'}),
        }

