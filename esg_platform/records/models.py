from django.db import models
from ingestion.models import RawUpload


class NormalizedRecord(models.Model):

    SOURCE_TYPES = (
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL"),
    )

    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("VALID", "VALID"),
        ("INVALID", "INVALID"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    )

    raw_upload = models.ForeignKey(
        RawUpload,
        on_delete=models.CASCADE,
        related_name="normalized_records"
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    quantity = models.FloatField(
        null=True,
        blank=True
    )

    cost_inr = models.FloatField(
        null=True,
        blank=True
    )

    unit = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    raw_data = models.JSONField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["source_type"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"{self.source_type} - {self.id}"