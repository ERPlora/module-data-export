from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

JOB_STATUS = [
    ('pending', _('Pending')),
    ('processing', _('Processing')),
    ('completed', _('Completed')),
    ('failed', _('Failed')),
]

class DataJob(HubBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    job_type = models.CharField(max_length=10, default='export', verbose_name=_('Job Type'))
    entity_type = models.CharField(max_length=100, verbose_name=_('Entity Type'))
    file_format = models.CharField(max_length=10, default='csv', verbose_name=_('File Format'))
    status = models.CharField(max_length=20, default='pending', choices=JOB_STATUS, verbose_name=_('Status'))
    records_count = models.PositiveIntegerField(default=0, verbose_name=_('Records Count'))
    file_path = models.CharField(max_length=500, blank=True, verbose_name=_('File Path'))
    error_message = models.TextField(blank=True, verbose_name=_('Error Message'))
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Completed At'))

    class Meta(HubBaseModel.Meta):
        db_table = 'data_export_datajob'

    def __str__(self):
        return self.name

