"""AI tools for the Data Export module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListDataJobs(AssistantTool):
    name = "list_data_jobs"
    description = "List data export/import jobs."
    module_id = "data_export"
    required_permission = "data_export.view_datajob"
    parameters = {
        "type": "object",
        "properties": {"status": {"type": "string"}, "job_type": {"type": "string", "description": "export, import"}, "entity_type": {"type": "string"}},
        "required": [],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from data_export.models import DataJob
        qs = DataJob.objects.all()
        if args.get('status'):
            qs = qs.filter(status=args['status'])
        if args.get('job_type'):
            qs = qs.filter(job_type=args['job_type'])
        if args.get('entity_type'):
            qs = qs.filter(entity_type=args['entity_type'])
        return {"jobs": [{"id": str(j.id), "name": j.name, "job_type": j.job_type, "entity_type": j.entity_type, "file_format": j.file_format, "status": j.status, "records_count": j.records_count} for j in qs.order_by('-created_at')[:20]]}


@register_tool
class GetDataJob(AssistantTool):
    name = "get_data_job"
    description = "Get details of a specific data export/import job."
    module_id = "data_export"
    required_permission = "data_export.view_datajob"
    parameters = {
        "type": "object",
        "properties": {"job_id": {"type": "string", "description": "Job ID"}},
        "required": ["job_id"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from data_export.models import DataJob
        j = DataJob.objects.get(id=args['job_id'])
        return {
            "id": str(j.id), "name": j.name, "job_type": j.job_type,
            "entity_type": j.entity_type, "file_format": j.file_format,
            "status": j.status, "records_count": j.records_count,
            "file_path": j.file_path if j.file_path else None,
            "error_message": j.error_message if j.error_message else None,
            "completed_at": j.completed_at.isoformat() if j.completed_at else None,
        }


@register_tool
class CreateExportJob(AssistantTool):
    name = "create_export_job"
    description = "Create a new data export job. Supported entities: products, customers, services, sales, invoices."
    module_id = "data_export"
    required_permission = "data_export.add_datajob"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Job name"},
            "entity_type": {"type": "string", "description": "Entity to export: products, customers, services, sales, invoices"},
            "file_format": {"type": "string", "description": "csv, xlsx, json (default: csv)"},
        },
        "required": ["entity_type"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from data_export.models import DataJob
        entity = args['entity_type']
        j = DataJob.objects.create(
            name=args.get('name', f'Export {entity}'),
            job_type='export',
            entity_type=entity,
            file_format=args.get('file_format', 'csv'),
            status='pending',
        )
        return {"id": str(j.id), "name": j.name, "status": "pending", "created": True}
