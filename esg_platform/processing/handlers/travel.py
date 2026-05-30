from processing.normalizers import normalize_number, normalize_text
from records.models import NormalizedRecord
from reviews.models import DataIssue


class TravelHandler:

    def process_row(self, upload, i, row):

        raw = {}

        for key, value in row.to_dict().items():
            if str(value) == "nan":
                raw[key] = None
            else:
                raw[key] = str(value)

        distance = normalize_number(row.get("distance_km"))
        cost = normalize_number(row.get("cost_inr"))
        travel_type = normalize_text(row.get("travel_type"))
        booking_status = normalize_text(row.get("booking_status"))

        is_valid = True

        # DISTANCE VALIDATION
        if distance is None:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="distance_km",
                issue_type="INVALID_TYPE",
                description="Distance missing or invalid",
                severity="HIGH"
            )

        elif distance <= 0:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="distance_km",
                issue_type="INVALID_VALUE",
                description="Distance must be greater than 0",
                severity="HIGH"
            )

        # COST VALIDATION
        if cost is None:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="cost_inr",
                issue_type="INVALID_TYPE",
                description="Invalid cost format",
                severity="HIGH"
            )

        elif cost <= 0:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="cost_inr",
                issue_type="INVALID_VALUE",
                description="Cost must be greater than 0",
                severity="HIGH"
            )

        # NORMALIZATION
        if travel_type:
            travel_type = travel_type.upper().strip()

        if booking_status:
            booking_status = booking_status.upper().strip()

        # SAVE RECORD ALWAYS
        NormalizedRecord.objects.create(
            raw_upload=upload,
            source_type="TRAVEL",
            quantity=distance,
            cost_inr=cost,
            unit=travel_type,
            raw_data=raw,
            status="VALID" if is_valid else "INVALID"
        )