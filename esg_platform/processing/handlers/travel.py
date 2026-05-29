from processing.normalizers import normalize_number, normalize_unit
from records.models import NormalizedRecord


class TravelHandler:

    def process_row(self, upload, i, row):

        distance = normalize_number(row.get("distance_km"))
        cost = normalize_number(row.get("cost_inr"))

        travel_type = normalize_unit(row.get("travel_type"))
        status_value = normalize_unit(row.get("booking_status"))

        issues = []

        # distance checks
        if distance is None:
            issues.append("Missing distance")

        elif distance < 0:
            issues.append("Negative distance found")

        elif distance == 0:
            issues.append("Distance must be greater than 0")

        # cost checks
        if cost is None:
            issues.append("Invalid cost format")

        elif cost < 0:
            issues.append("Cost cannot be negative")

        status = "INVALID" if issues else "VALID"

        NormalizedRecord.objects.create(
            raw_upload=upload,
            source_type="TRAVEL",
            quantity=distance,
            cost_inr=cost,
            unit=travel_type,
            status=status,
            issues=", ".join(issues),
            raw_data=row.to_dict()
        )