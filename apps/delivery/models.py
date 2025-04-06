from django.contrib.auth.models import User
from django.db import models

from apps.warehouses.models import Warehouse
from core.models import BaseModel


# Create your models here.
class Delivery(BaseModel):
    person_assigned = models.ForeignKey(
        User, related_name="delivery_assigned", on_delete=models.CASCADE
    )
    date_assigned = models.DateTimeField(auto_now_add=True)
    date_delivered = models.DateTimeField(auto_now=True)
    estimated_time_arrival = models.DateTimeField(verbose_name="ETA")
    is_delivered = models.BooleanField(default=False)
    delivery_address = models.TextField(max_length=155)

    destination_warehouses = models.ManyToManyField(Warehouse, related_name="deliveries")

    def __str__(self):
        return f"Delivery to {self.destination_warehouses.count()} warehouses"