from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DataExportConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'data_export'
    label = 'data_export'
    verbose_name = _('Data Import/Export')

    def ready(self):
        pass
