"""
Data Import/Export Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required, permission_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import DataJob

PER_PAGE_CHOICES = [12, 24, 48, 96, 0]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('data_export', 'dashboard')
@htmx_view('data_export/pages/index.html', 'data_export/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_data_jobs': DataJob.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# DataJob
# ======================================================================

DATA_JOB_SORT_FIELDS = {
    'name': 'name',
    'status': 'status',
    'records_count': 'records_count',
    'job_type': 'job_type',
    'entity_type': 'entity_type',
    'file_format': 'file_format',
    'created_at': 'created_at',
}

def _build_data_jobs_context(hub_id, per_page=10):
    qs = DataJob.objects.filter(hub_id=hub_id, is_deleted=False).order_by('name')
    paginator = Paginator(qs, per_page if per_page > 0 else max(qs.count(), 1))
    page_obj = paginator.get_page(1)
    return {
        'data_jobs': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'name',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_data_jobs_list(request, hub_id, per_page=10):
    ctx = _build_data_jobs_context(hub_id, per_page)
    return django_render(request, 'data_export/partials/data_jobs_list.html', ctx)

@login_required
@with_module_nav('data_export', 'import')
@htmx_view('data_export/pages/data_jobs.html', 'data_export/partials/data_jobs_content.html')
def data_jobs_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'name')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 12))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 12

    qs = DataJob.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(name__icontains=search_query) | Q(job_type__icontains=search_query) | Q(entity_type__icontains=search_query) | Q(file_format__icontains=search_query))

    order_by = DATA_JOB_SORT_FIELDS.get(sort_field, 'name')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['name', 'status', 'records_count', 'job_type', 'entity_type', 'file_format']
        headers = ['Name', 'Status', 'Records Count', 'Job Type', 'Entity Type', 'File Format']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='data_jobs.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='data_jobs.xlsx')

    paginator = Paginator(qs, per_page if per_page > 0 else max(qs.count(), 1))
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'data_export/partials/data_jobs_list.html', {
            'data_jobs': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'data_jobs': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
@htmx_view('data_export/pages/data_job_add.html', 'data_export/partials/data_job_add_content.html')
def data_job_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        job_type = request.POST.get('job_type', '').strip()
        entity_type = request.POST.get('entity_type', '').strip()
        file_format = request.POST.get('file_format', '').strip()
        status = request.POST.get('status', '').strip()
        records_count = int(request.POST.get('records_count', 0) or 0)
        file_path = request.POST.get('file_path', '').strip()
        error_message = request.POST.get('error_message', '').strip()
        completed_at = request.POST.get('completed_at') or None
        obj = DataJob(hub_id=hub_id)
        obj.name = name
        obj.job_type = job_type
        obj.entity_type = entity_type
        obj.file_format = file_format
        obj.status = status
        obj.records_count = records_count
        obj.file_path = file_path
        obj.error_message = error_message
        obj.completed_at = completed_at
        obj.save()
        response = HttpResponse(status=204)
        response['HX-Redirect'] = reverse('data_export:data_jobs_list')
        return response
    return {}

@login_required
@htmx_view('data_export/pages/data_job_edit.html', 'data_export/partials/data_job_edit_content.html')
def data_job_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(DataJob, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '').strip()
        obj.job_type = request.POST.get('job_type', '').strip()
        obj.entity_type = request.POST.get('entity_type', '').strip()
        obj.file_format = request.POST.get('file_format', '').strip()
        obj.status = request.POST.get('status', '').strip()
        obj.records_count = int(request.POST.get('records_count', 0) or 0)
        obj.file_path = request.POST.get('file_path', '').strip()
        obj.error_message = request.POST.get('error_message', '').strip()
        obj.completed_at = request.POST.get('completed_at') or None
        obj.save()
        return _render_data_jobs_list(request, hub_id)
    return {'obj': obj}

@login_required
@require_POST
def data_job_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(DataJob, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_data_jobs_list(request, hub_id)

@login_required
@require_POST
def data_jobs_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = DataJob.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_data_jobs_list(request, hub_id)


@login_required
@permission_required('data_export.manage_settings')
@with_module_nav('data_export', 'settings')
@htmx_view('data_export/pages/settings.html', 'data_export/partials/settings_content.html')
def settings_view(request):
    return {}

