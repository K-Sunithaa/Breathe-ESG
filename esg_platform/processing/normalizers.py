def normalize_number(value):
    try:
        if value is None:
            return None

        value = str(value).replace(",", "").strip()

        if value.lower() in ["null", "none", "", "invalid_cost"]:
            return None

        return float(value)
    except:
        return None


def normalize_text(value):
    if value in ["NULL", "null", "", None]:
        return None
    return str(value).strip()


def normalize_unit(value):
    if not value:
        return None

    value = str(value).strip().upper()

    mapping = {
        "LITER": "L",
        "LITRE": "L",
        "LT": "L",
        "KWH": "KWH",
        "UNITS": "UNIT",
        "UNIT": "UNIT",
        "TAXI": "CAB",
        "CAB": "CAB",
        "FLIGHT": "FLIGHT",
        "TRAIN": "TRAIN"
    }

    return mapping.get(value, value)