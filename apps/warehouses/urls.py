from django.urls import path

from apps.warehouses.views import WarehouseListView

urlpatterns = [
    path("warehouses/", WarehouseListView.as_view(), name="warehouse-list"),
]