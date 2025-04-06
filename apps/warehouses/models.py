from django.db import models

from core.models import BaseModel

from .utils import validate_geotag


class Warehouse(BaseModel):
    code = models.CharField(unique=True, max_length=10)
    warehouse_name = models.CharField(max_length=255)
    warehouse_address = models.TextField()
    warehouse_geotag = models.CharField(
        max_length=40,
        validators=[validate_geotag],
        help_text="Format: 'latitude, longitude'",  # Format: "latitude, longitude"
    )

    def __str__(self):
        return self.warehouse_name
