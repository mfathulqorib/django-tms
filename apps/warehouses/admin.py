from django.contrib import admin

from apps.warehouses.models import Warehouse

# Register your models here.


class WarehouseAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "actor", "name")


admin.site.register(Warehouse, WarehouseAdmin)
