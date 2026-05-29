def validate_required(value):
    return value is not None


def validate_positive(value):
    if value is None:
        return False
    return value > 0