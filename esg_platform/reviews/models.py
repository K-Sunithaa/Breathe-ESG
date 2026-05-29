from django.db import models
from ingestion.models import RawUpload


class DataIssue(models.Model):

    SEVERITY_CHOICES = (
        ("LOW", "LOW"),
        ("MEDIUM", "MEDIUM"),
        ("HIGH", "HIGH"),
    )

    ISSUE_TYPES = (
        ("MISSING", "MISSING"),
        ("INVALID", "INVALID"),
        ("INVALID_VALUE", "INVALID_VALUE"),
        ("INVALID_TYPE", "INVALID_TYPE"),
    )

    raw_upload = models.ForeignKey(RawUpload, on_delete=models.CASCADE)
    row_number = models.IntegerField()
    field_name = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=50, choices=ISSUE_TYPES)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    resolved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class RecordReview(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    )

    record_id = models.IntegerField()  # or FK to NormalizedRecord

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    reviewer_comment = models.TextField(null=True, blank=True)

    reviewed_at = models.DateTimeField(null=True, blank=True)
