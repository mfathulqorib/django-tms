import re

from django.core.exceptions import ValidationError


def validate_geotag(value):
    # regex for check format latitude, longitude
    pattern = r"^-?\d{1,2}(\.\d+)?,\s*-?\d{1,3}(\.\d+)?$"

    if not re.match(pattern, value):
        raise ValidationError(
            "Geotag must be in 'latitude, longitude' format (e.g., 12.3456, -98.7654)."
        )
