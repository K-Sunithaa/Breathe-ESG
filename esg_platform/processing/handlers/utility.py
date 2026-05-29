from processing.normalizers import normalize_number, normalize_unit
from records.models import NormalizedRecord


class UtilityHandler:

    def process_row(self, upload, i, row):

        units = normalize_number(row.get("units_consumed"))
        cost = normalize_number(row.get("cost"))
        unit = normalize_unit(row.get("unit"))

        issues = []

        # units checks
        if units is None:
            issues.append("Missing units consumed")

        elif units < 0:
            issues.append("Negative units found")

        elif units == 0:
            issues.append("Units must be greater than 0")

        # cost checks
        if cost is None:
            issues.append("Invalid cost format")

        elif cost < 0:
            issues.append("Cost cannot be negative")

        status = "INVALID" if issues else "VALID"

        NormalizedRecord.objects.create(
            raw_upload=upload,
            source_type="UTILITY",
            quantity=units,
            cost_inr=cost,
            unit=unit,
            status=status,
            issues=", ".join(issues),
            raw_data=row.to_dict()
        )