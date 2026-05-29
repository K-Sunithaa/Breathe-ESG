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
            "source_type": record.source_type,
            "quantity": record.quantity,
            "cost_inr": record.cost_inr,
            "unit": record.unit,
            "status": record.status,
            "created_at": record.created_at,
            "raw_data": record.raw_data,
        })

    return Response(data)