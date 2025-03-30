from django.contrib.auth.models import User
from django.db import models
from core.models import BaseModel
from core.utils import generate_id

# Create your models here.
class ProfileUser(models.Model):
    id = models.CharField(primary_key=True, default=generate_id, editable=False, max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    warehouse_location = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username