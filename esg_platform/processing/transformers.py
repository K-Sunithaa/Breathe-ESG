# =========================
# COMMON VALUE TRANSFORMERS
# =========================

def normalize_number(value):
    """
    Converts:
    - "1,200"
    - "1200 INR"
    - "NULL"
    - "invalid_cost"

    into clean float values
    """

    try:
        if value is None:
            return None

        value = str(value).strip().upper()

        # invalid placeholders
        invalid_values = [
            "NULL",
            "NONE",
            "",
            "INVALID_COST",
            "N/A"
        ]

        if value in invalid_values:
            return None

        # remove commas + currency text
        value = value.replace(",", "")
        value = value.replace("INR", "")
        value = value.replace("₹", "")
        value = value.replace("KWH", "")
        value = value.replace("UNITS", "")

        value = value.strip()

        return float(value)

    except:
        return None


# =========================
# NULL NORMALIZATION
# =========================
def normalize_null(value):

    if value is None:
        return None

    value = str(value).strip()

    if value.upper() in ["NULL", "NONE", ""]:
        return None

    return value


# =========================
# SAP UNIT NORMALIZATION
# =========================
def normalize_sap_unit(unit):

    unit = normalize_null(unit)

    if not unit:
        return None

    unit = unit.upper()

    mapping = {
        "LITER": "L",
        "LITRE": "L",
        "LT": "L",
        "KILOGRAM": "KG",
        "KG": "KG"
    }

    return mapping.get(unit, unit)


# =========================
# UTILITY UNIT NORMALIZATION
# =========================
def normalize_utility_unit(unit):

    unit = normalize_null(unit)

    if not unit:
        return None

    unit = unit.upper()

    mapping = {
        "KWH": "KWH",
        "KILOWATT": "KWH",
        "UNIT": "UNIT",
        "UNITS": "UNIT"
    }

    return mapping.get(unit, unit)


# =========================
# TRAVEL TYPE NORMALIZATION
# =========================
def normalize_travel_type(value):

    value = normalize_null(value)

    if not value:
        return None

    value = value.upper()

    mapping = {
        "FLIGHT": "FLIGHT",
        "AIR": "FLIGHT",
        "TRAIN": "TRAIN",
        "RAIL": "TRAIN",
        "TAXI": "CAB",
        "CAB": "CAB"
    }

    return mapping.get(value, value)


# =========================
# BOOKING STATUS NORMALIZATION
# =========================
def normalize_status(value):

    value = normalize_null(value)

    if not value:
        return None

    value = value.upper()

    mapping = {
        "BOOKED": "BOOKED",
        "COMPLETED": "COMPLETED",
        "CANCELLED": "CANCELLED"
    }

    return mapping.get(value, value)