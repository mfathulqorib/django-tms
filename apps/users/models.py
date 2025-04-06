from django.contrib.auth.models import User
from django.db import models

from apps.warehouses.models import Warehouse
from core.models import BaseModel


# Create your models here.
class ProfileUser(BaseModel):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True)
    warehouse = models.ForeignKey(
        Warehouse, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.user.username
