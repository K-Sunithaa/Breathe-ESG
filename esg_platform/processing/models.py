from django.db import models
from ingestion.models import RawUpload


class ProcessingLog(models.Model):

    STATUS_CHOICES = (
        ("STARTED", "STARTED"),
        ("SUCCESS", "SUCCESS"),
        ("FAILED", "FAILED"),
    )

    raw_upload = models.ForeignKey(
        RawUpload,
        on_delete=models.CASCADE,
        related_name="processing_logs"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    message = models.TextField(null=True, blank=True)

    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.raw_upload_id} - {self.status}"