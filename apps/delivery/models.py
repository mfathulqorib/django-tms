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
    date_delivered = models.DateTimeField(null=True, blank=True)
    estimated_time_arrival = models.DateField(verbose_name="ETA")
    delivery_notes = models.TextField(max_length=155, null=True, blank=True)
    destination_warehouses = models.ManyToManyField(
        Warehouse, related_name="deliveries"
    )

    is_delivered = models.BooleanField(default=False)

    def __str__(self):
        if self.pk:  # safe check
            return f"Delivery to {self.destination_warehouses.count()} warehouses"
        return "New Delivery"