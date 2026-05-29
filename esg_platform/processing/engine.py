import pandas as pd
import logging

from ingestion.models import RawUpload
from processing.registry import get_handler

logger = logging.getLogger(__name__)


def process_file(upload_id):

    upload = RawUpload.objects.get(id=upload_id)

    path = upload.file.path
    source = upload.source_type.upper()

    logger.info(f"Processing started: {source}")

    upload.status = "PROCESSING"
    upload.save()

    try:
        # -------------------------
        # LOAD FILE SAFELY
        # -------------------------
        if path.endswith(".csv"):
            df = pd.read_csv(path)
        else:
            df = pd.read_excel(path)

        # -------------------------
        # GET HANDLER
        # -------------------------
        handler = get_handler(source)

        if handler is None:
            raise ValueError(f"No handler found for source: {source}")

        # -------------------------
        # PROCESS ROWS
        # -------------------------
        for i, row in df.iterrows():
            handler.process_row(upload, i, row)

        # SUCCESS
        upload.status = "DONE"

    except Exception as e:
        logger.error(f"Processing failed: {str(e)}")
        upload.status = "FAILED"

    finally:
        upload.save()