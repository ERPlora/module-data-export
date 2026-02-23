from django.utils.translation import gettext_lazy as _

MODULE_ID = 'data_export'
MODULE_NAME = _('Data Import/Export')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'cloud-download-outline'
MODULE_DESCRIPTION = _('Data import and export in multiple formats')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'analytics'

MENU = {
    'label': _('Data Import/Export'),
    'icon': 'cloud-download-outline',
    'order': 76,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Import'), 'icon': 'cloud-upload-outline', 'id': 'import'},
{'label': _('Export'), 'icon': 'cloud-download-outline', 'id': 'export'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'data_export.view_datajob',
'data_export.run_import',
'data_export.run_export',
'data_export.manage_settings',
]
