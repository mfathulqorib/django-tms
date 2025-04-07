from django.urls import path

from apps.delivery.views import (
    DeliveryCreateView,
    DeliveryListView,
    DeliveryUpdateView,
    HistoryDeliveryListView,
    HistoryDeliveryUpdateView,
)

urlpatterns = [
    path("delivery/", DeliveryListView.as_view(), name="list-delivery"),
    path("delivery/create/", DeliveryCreateView.as_view(), name="create-delivery"),
    path(
        "delivery/history/",
        HistoryDeliveryListView.as_view(),
        name="list-delivery-history",
    ),
    path("delivery/<str:id>/", DeliveryUpdateView.as_view(), name="update-delivery"),
    path(
        "delivery/history/<str:id>/",
        HistoryDeliveryUpdateView.as_view(),
        name="update-delivery-history",
    ),
]
