from django.contrib import admin

from apps.delivery.models import Delivery

# Register your models here.


class DeliveryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "person_assigned",
        "date_assigned",
        "estimated_time_arrival",
        "is_delivered",
    )


admin.site.register(Delivery, DeliveryAdmin)
