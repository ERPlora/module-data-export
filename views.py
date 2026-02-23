"""
Data Import/Export Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('data_export', 'dashboard')
@htmx_view('data_export/pages/dashboard.html', 'data_export/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('data_export', 'import')
@htmx_view('data_export/pages/import.html', 'data_export/partials/import_content.html')
def import(request):
    """Import view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('data_export', 'export')
@htmx_view('data_export/pages/export.html', 'data_export/partials/export_content.html')
def export(request):
    """Export view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('data_export', 'settings')
@htmx_view('data_export/pages/settings.html', 'data_export/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

