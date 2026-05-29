from celery import shared_task
from processing.engine import process_file

@shared_task
def process_file_task(upload_id):
    process_file(upload_id)