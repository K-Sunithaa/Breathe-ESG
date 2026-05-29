from django.db import models
from ingestion.models import RawUpload


class STATUS_CHOICES(models.TextChoices):
    VALID = "VALID", "VALID"
    INVALID = "INVALID", "INVALID"


class NormalizedRecord(models.Model):

    raw_upload = models.ForeignKey(
        RawUpload,
        on_delete=models.CASCADE,
        related_name="normalized_records"
    )

    source_type = models.CharField(
        max_length=50
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
        choices=STATUS_CHOICES.choices,
        default=STATUS_CHOICES.VALID
    )

    # ✅ THIS IS THE IMPORTANT FIX YOU NEEDED
    issues = models.TextField(
        null=True,
        blank=True,
        help_text="Comma-separated list of validation issues found during normalization"
    )

    raw_data = models.JSONField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["source_type"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return f"{self.source_type} - {self.status}"