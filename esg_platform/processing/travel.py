from processing.normalizers import normalize_number, normalize_text
from reviews.models import DataIssue
from records.models import NormalizedRecord


class TravelHandler:

    def process_row(self, upload, i, row):

        distance = normalize_number(row.get("distance_km"))
        cost = normalize_number(row.get("cost_inr"))
        travel_type = normalize_text(row.get("travel_type"))

        is_valid = True

        if cost is None:
            is_valid = False
            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="cost_inr",
                issue_type="INVALID",
                description="Invalid cost",
                severity="HIGH"
            )

        if is_valid:
            NormalizedRecord.objects.create(
                raw_upload=upload,
                source_type="TRAVEL",
                quantity=distance,
                cost_inr=cost,
                unit=travel_type,
                raw_data=row.to_dict()
            )