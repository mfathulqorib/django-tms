from django.db import models
from django.contrib.auth.models import User
from core.models import BaseModel


class Warehouse(BaseModel):
    warehouse_name = models.CharField(max_length=255)
    warehouse_address = models.TextField()
    warehouse_geotag = models.CharField(max_length=100)  # Format: "latitude,longitude"