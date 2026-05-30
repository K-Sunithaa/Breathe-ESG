from django.db import models
from ingestion.models import RawUpload


class NormalizedRecord(models.Model):

    SOURCE_TYPES = (
        ("SAP", "SAP"),
        ("UTILITY", "UTILITY"),
        ("TRAVEL", "TRAVEL"),
    )

    SCOPE_CHOICES = (
        ("SCOPE_1", "Scope 1"),
        ("SCOPE_2", "Scope 2"),
        ("SCOPE_3", "Scope 3"),
    )

    STATUS_CHOICES = (
        ("PENDING", "PENDING"),
        ("VALID", "VALID"),
        ("INVALID", "INVALID"),
        ("UNDER_REVIEW", "UNDER_REVIEW"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("LOCKED", "LOCKED"),
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

    # Added for Breathe ESG assignment

    tenant_id = models.CharField(
        max_length=100,
        default="default_tenant"
    )

    scope_category = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES,
        default="SCOPE_1"
    )

    activity_type = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    source_system = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    source_record_id = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    source_file_name = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    quantity = models.FloatField(
        null=True,
        blank=True
    )

    cost_inr = models.FloatField(
        null=True,
        blank=True
    )

    # Existing field
    unit = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    # Added for normalization tracking
    normalized_unit = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    facility_code = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    plant_code = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    billing_period_start = models.DateField(
        blank=True,
        null=True
    )

    billing_period_end = models.DateField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING"
    )

    locked_for_audit = models.BooleanField(
        default=False
    )

    raw_data = models.JSONField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        indexes = [
            models.Index(fields=["source_type"]),
            models.Index(fields=["status"]),
            models.Index(fields=["scope_category"]),
        ]

    def __str__(self):
        return f"{self.source_type} - {self.id}"


class AuditLog(models.Model):

    ACTION_CHOICES = (
        ("UPLOAD", "UPLOAD"),
        ("NORMALIZED", "NORMALIZED"),
        ("ISSUE_CREATED", "ISSUE_CREATED"),
        ("REVIEWED", "REVIEWED"),
        ("APPROVED", "APPROVED"),
        ("REJECTED", "REJECTED"),
        ("LOCKED", "LOCKED"),
    )

    record = models.ForeignKey(
        NormalizedRecord,
        on_delete=models.CASCADE,
        related_name="audit_logs"
    )

    action = models.CharField(
        max_length=50,
        choices=ACTION_CHOICES
    )

    performed_by = models.CharField(
        max_length=100,
        blank=True
    )

    notes = models.TextField(
        blank=True
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.record.id} - {self.action}"