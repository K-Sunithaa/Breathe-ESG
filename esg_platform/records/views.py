from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import NormalizedRecord


@api_view(["GET"])
def get_records(request):

    records = NormalizedRecord.objects.all().order_by("-created_at")

    data = []

    for record in records:
        data.append({
            "id": record.id,

            # Source Information
            "source_type": record.source_type,
            "source_system": record.source_system,
            "source_record_id": record.source_record_id,
            "source_file_name": record.source_file_name,

            # Multi-tenancy
            "tenant_id": record.tenant_id,

            # ESG Fields
            "scope_category": record.scope_category,
            "activity_type": record.activity_type,

            # Quantities
            "quantity": record.quantity,
            "cost_inr": record.cost_inr,

            # Units
            "unit": record.unit,
            "normalized_unit": record.normalized_unit,

            # Facility Information
            "facility_code": record.facility_code,
            "plant_code": record.plant_code,

            # Billing Period
            "billing_period_start": record.billing_period_start,
            "billing_period_end": record.billing_period_end,

            # Status
            "status": record.status,
            "locked_for_audit": record.locked_for_audit,

            # Metadata
            "created_at": record.created_at,
            "updated_at": record.updated_at,

            # Original Data
            "raw_data": record.raw_data,
        })

    return Response(data)