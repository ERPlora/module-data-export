# Data Import/Export Module

Data import and export in multiple formats.

## Features

- Import and export data for various entity types
- Support for multiple file formats (CSV, and others)
- Track job status through lifecycle: Pending, Processing, Completed, Failed
- Record count tracking per job
- Error message capture for failed jobs
- File path storage for generated export files
- Completion timestamp tracking
- Dashboard overview of import/export activity

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Data Import/Export > Settings**

## Usage

Access via: **Menu > Data Import/Export**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/data_export/dashboard/` | Overview of recent import/export jobs |
| Import | `/m/data_export/import/` | Run data import jobs |
| Export | `/m/data_export/export/` | Run data export jobs |
| Settings | `/m/data_export/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `DataJob` | An import or export job with name, type (import/export), entity type, file format, status, record count, file path, error message, and completion timestamp |

## Permissions

| Permission | Description |
|------------|-------------|
| `data_export.view_datajob` | View import/export jobs |
| `data_export.run_import` | Run data import jobs |
| `data_export.run_export` | Run data export jobs |
| `data_export.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
