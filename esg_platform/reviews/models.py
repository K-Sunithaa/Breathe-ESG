from django.db import models
from ingestion.models import RawUpload
from records.models import NormalizedRecord


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
        ("SUSPICIOUS", "SUSPICIOUS"),
    )

    raw_upload = models.ForeignKey(
        RawUpload,
        on_delete=models.CASCADE
    )

    record = models.ForeignKey(
        NormalizedRecord,
        on_delete=models.CASCADE,
        related_name="issues",
        null=True,
        blank=True
    )

    row_number = models.IntegerField()

    field_name = models.CharField(
        max_length=100
    )

    issue_type = models.CharField(
        max_length=50,
        choices=ISSUE_TYPES
    )

    description = models.TextField()

    severity = models.CharField(
        max_length=10,
        choices=SEVERITY_CHOICES
    )

    resolved = models.BooleanField(
        default=False
    )

    assigned_to = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    resolved_by = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    resolved_at = models.DateTimeField(
        null=True,
        blank=True
    )

    resolution_note = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.issue_type} - Row {self.row_number}"


class RecordReview(models.Model):

    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
    )

    record = models.ForeignKey(
        NormalizedRecord,
        on_delete=models.CASCADE,
        related_name="reviews",
        null=True,
        blank=True
    )

    reviewer_name = models.CharField(
        max_length=100,
        default="Analyst"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    review_round = models.IntegerField(
        default=1
    )

    reviewer_comment = models.TextField(
        null=True,
        blank=True
    )

    decision_reason = models.TextField(
        blank=True,
        null=True
    )

    reviewed_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        record_id = self.record.id if self.record else "No Record"
        return f"{record_id} - {self.status}"