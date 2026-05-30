from ingestion.models import RawUpload
from processing.tasks import process_file_task  # ✅ IMPORT CELERY TASK

def ingest_file(file_obj, source_type):

    upload = RawUpload.objects.create(
        file=file_obj,
        source_type=source_type,
        status="UPLOADED"
    )

    # 🚀 STEP 6: SEND TO CELERY (ASYNC)
    process_file_task.delay(upload.id)

    return {
        "upload_id": upload.id,
        "status": "processing started"
    }