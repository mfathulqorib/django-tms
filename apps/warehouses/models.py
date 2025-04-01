from django.contrib.auth.models import User
from django.db import models

from core.models import BaseModel

from .utils import validate_geotag


class Warehouse(BaseModel):
    warehouse_name = models.CharField(max_length=255)
    warehouse_address = models.TextField()
    warehouse_geotag = models.CharField(
        max_length=40, validators=[validate_geotag]  # Format: "latitude, longitude"
    )
