from django.urls import path

from apps.warehouses.views import WarehouseListView, WarehouseCreateView, WarehouseDeleteView

urlpatterns = [
    path("warehouses/", WarehouseListView.as_view(), name="warehouse-list"),
    path("detail-warehouse/", WarehouseCreateView.as_view(), name="detail-warehouse"),
    path("detail-warehouse/<str:id>/delete/", WarehouseDeleteView.as_view(), name="delete-warehouse"),
]