from django.urls import path

from apps.warehouses.views import WarehouseListView, WarehouseCreateView

urlpatterns = [
    path("warehouses/", WarehouseListView.as_view(), name="warehouse-list"),
    path("create-warehouses/", WarehouseCreateView.as_view(), name="create-warehouse"),
]