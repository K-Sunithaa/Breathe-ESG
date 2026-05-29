from processing.normalizers import normalize_number, normalize_text
from records.models import NormalizedRecord


class SAPHandler:

    def process_row(self, upload, i, row):

        qty = normalize_number(row.get("quantity"))
        cost = normalize_number(row.get("cost_inr"))
        unit = normalize_text(row.get("unit"))

        issues = []

        # quantity checks
        if qty is None:
            issues.append("Missing quantity")

        elif qty < 0:
            issues.append("Negative quantity found")

        elif qty == 0:
            issues.append("Quantity must be greater than 0")

        # cost checks
        if cost is None:
            issues.append("Invalid cost format")

        elif cost < 0:
            issues.append("Cost cannot be negative")

        # unit normalization
        if unit:
            unit = unit.upper()

            if unit in ["LITER", "LITRE", "LT"]:
                unit = "L"

        status = "INVALID" if issues else "VALID"

        NormalizedRecord.objects.create(
            raw_upload=upload,
            source_type="SAP",
            quantity=qty,
            cost_inr=cost,
            unit=unit,
            status=status,
            issues=", ".join(issues),
            raw_data=row.to_dict()
        )