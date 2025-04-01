from django.urls import path

from apps.warehouses.views import WarehouseListView, WarehouseCreateView, WarehouseDeleteView, WarehouseUpdateView

urlpatterns = [
    path("warehouses/", WarehouseListView.as_view(), name="warehouse-list"),
    path("warehouse/create/", WarehouseCreateView.as_view(), name='create-warehouse'),
    path("warehouse/<str:id>/", WarehouseUpdateView.as_view(), name="detail-warehouse"),
    path("warehouse/<str:id>/delete/", WarehouseDeleteView.as_view(), name="delete-warehouse"),
]