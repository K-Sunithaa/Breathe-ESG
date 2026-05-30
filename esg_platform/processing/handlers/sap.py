from processing.normalizers import normalize_number, normalize_text
from records.models import NormalizedRecord
from reviews.models import DataIssue


class SAPHandler:

    def process_row(self, upload, i, row):

        raw = {}

        for key, value in row.to_dict().items():
            if str(value) == "nan":
                raw[key] = None
            else:
                raw[key] = str(value)

        qty = normalize_number(row.get("quantity"))
        cost = normalize_number(row.get("cost_inr"))
        unit = normalize_text(row.get("unit"))

        is_valid = True

        # QUANTITY VALIDATION
        if qty is None:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="quantity",
                issue_type="MISSING_VALUE",
                description="Quantity missing or invalid",
                severity="HIGH"
            )

        elif qty <= 0:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="quantity",
                issue_type="INVALID_VALUE",
                description="Quantity must be greater than 0",
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

        # UNIT NORMALIZATION
        if unit:
            unit = unit.upper().strip()

            if unit in ["LITER", "LITRE", "LT"]:
                unit = "L"

        # SAVE RECORD ALWAYS
        NormalizedRecord.objects.create(
            raw_upload=upload,
            source_type="SAP",
            quantity=qty,
            cost_inr=cost,
            unit=unit,
            raw_data=raw,
            status="VALID" if is_valid else "INVALID"
        )