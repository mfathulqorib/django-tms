from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    geotag = models.CharField(max_length=100)  # Format: "latitude,longitude"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name