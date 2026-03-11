"""
AI context for the Data Export module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Data Export

### Models

**DataJob** — a single export (or import) job that processes entity data to/from a file.
- `name` (str): descriptive job name (e.g. "Products export - March 2026")
- `job_type` (str, default "export"): "export" or "import"
- `entity_type` (str, max 100): the data being processed (e.g. "inventory.Product", "customers.Customer", "sales.Sale")
- `file_format` (str, default "csv"): output format — "csv", "xlsx", "json", "xml"
- `status` (choice): pending → processing → completed / failed
- `records_count` (int, default 0): how many records were processed
- `file_path` (str, max 500): path to the generated file (populated on completion)
- `error_message` (text): details if status="failed"
- `completed_at` (datetime, nullable): when the job finished

### Key flows

1. **Start an export**: create a DataJob with job_type="export", entity_type, file_format, status="pending".
2. **Processing**: update status="processing" when the task begins.
3. **Complete**: set status="completed", file_path to the output file, records_count to number of rows, completed_at=now.
4. **Handle failure**: set status="failed", error_message with the traceback or reason.
5. **Check pending jobs**: filter by status="pending" or status="processing".
6. **Download**: retrieve file_path to serve the generated file to the user.

### Notes
- entity_type follows the `"app_label.ModelName"` convention.
- Jobs are asynchronous — they are created with status="pending" and processed in the background.
"""
