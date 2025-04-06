from django.urls import path

from apps.delivery.views import DeliveryCreateView, DeliveryListView

urlpatterns = [
    path("delivery/", DeliveryListView.as_view(), name="list-delivery"),
    path("delivery/create/", DeliveryCreateView.as_view(), name="create-delivery"),
]
