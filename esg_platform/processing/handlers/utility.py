from processing.normalizers import normalize_number, normalize_text
from records.models import NormalizedRecord
from reviews.models import DataIssue


class UtilityHandler:

    def process_row(self, upload, i, row):

        raw = {}

        for key, value in row.to_dict().items():
            if str(value) == "nan":
                raw[key] = None
            else:
                raw[key] = str(value)

        units = normalize_number(row.get("units_consumed"))
        cost = normalize_number(row.get("cost"))
        unit = normalize_text(row.get("unit"))

        is_valid = True

        # UNITS VALIDATION
        if units is None:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="units_consumed",
                issue_type="MISSING_VALUE",
                description="Units missing or invalid",
                severity="HIGH"
            )

        elif units <= 0:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="units_consumed",
                issue_type="INVALID_VALUE",
                description="Units must be greater than 0",
                severity="HIGH"
            )

        # COST VALIDATION
        if cost is None:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="cost",
                issue_type="INVALID_TYPE",
                description="Invalid cost format",
                severity="HIGH"
            )

        elif cost <= 0:
            is_valid = False

            DataIssue.objects.create(
                raw_upload=upload,
                row_number=i,
                field_name="cost",
                issue_type="INVALID_VALUE",
                description="Cost must be greater than 0",
                severity="HIGH"
            )

        # UNIT NORMALIZATION
        if unit:
            unit = unit.upper().strip()

        # SAVE RECORD ALWAYS
        NormalizedRecord.objects.create(
            raw_upload=upload,
            source_type="UTILITY",
            quantity=units,
            cost_inr=cost,
            unit=unit,
            raw_data=raw,
            status="VALID" if is_valid else "INVALID"
        )