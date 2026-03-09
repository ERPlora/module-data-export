# Data Import/Export

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `data_export` |
| **Version** | `1.0.0` |
| **Icon** | `cloud-download-outline` |
| **Dependencies** | None |

## Models

### `DataJob`

DataJob(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, name, job_type, entity_type, file_format, status, records_count, file_path, error_message, completed_at)

| Field | Type | Details |
|-------|------|---------|
| `name` | CharField | max_length=255 |
| `job_type` | CharField | max_length=10 |
| `entity_type` | CharField | max_length=100 |
| `file_format` | CharField | max_length=10 |
| `status` | CharField | max_length=20, choices: pending, processing, completed, failed |
| `records_count` | PositiveIntegerField |  |
| `file_path` | CharField | max_length=500, optional |
| `error_message` | TextField | optional |
| `completed_at` | DateTimeField | optional |

## URL Endpoints

Base path: `/m/data_export/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `import/` | `import` | GET/POST |
| `export/` | `export` | GET |
| `data_jobs/` | `data_jobs_list` | GET |
| `data_jobs/add/` | `data_job_add` | GET/POST |
| `data_jobs/<uuid:pk>/edit/` | `data_job_edit` | GET |
| `data_jobs/<uuid:pk>/delete/` | `data_job_delete` | GET/POST |
| `data_jobs/bulk/` | `data_jobs_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `data_export.view_datajob` | View Datajob |
| `data_export.run_import` | Run Import |
| `data_export.run_export` | Run Export |
| `data_export.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `run_export`, `run_import`, `view_datajob`
- **employee**: `view_datajob`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Import | `cloud-upload-outline` | `import` | No |
| Export | `cloud-download-outline` | `export` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_data_jobs`

List data export/import jobs.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `status` | string | No |  |
| `job_type` | string | No | export, import |
| `entity_type` | string | No |  |

### `get_data_job`

Get details of a specific data export/import job.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `job_id` | string | Yes | Job ID |

### `create_export_job`

Create a new data export job. Supported entities: products, customers, services, sales, invoices.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | No | Job name |
| `entity_type` | string | Yes | Entity to export: products, customers, services, sales, invoices |
| `file_format` | string | No | csv, xlsx, json (default: csv) |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  data_export/
    css/
    js/
  icons/
    icon.svg
templates/
  data_export/
    pages/
      dashboard.html
      data_job_add.html
      data_job_edit.html
      data_jobs.html
      export.html
      import.html
      index.html
      settings.html
    partials/
      dashboard_content.html
      data_job_add_content.html
      data_job_edit_content.html
      data_jobs_content.html
      data_jobs_list.html
      export_content.html
      import_content.html
      panel_data_job_add.html
      panel_data_job_edit.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
