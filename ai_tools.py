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
