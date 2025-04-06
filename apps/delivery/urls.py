from django.urls import path

from apps.delivery.views import DeliveryCreateView, DeliveryListView

urlpatterns = [
    path("delivery/", DeliveryListView.as_view(), name="delivery-list"),
    path("delivery/create/", DeliveryCreateView.as_view(), name="delivery-create"),
]
