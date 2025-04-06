from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import ListView, View

from apps.users.models import ProfileUser
from apps.warehouses.models import Warehouse

from .models import Delivery

# Create your views here.


class DeliveryListView(ListView, LoginRequiredMixin):
    model = Delivery
    template_name = "delivery/list_delivery.html"
    context_object_name = "delivery_list"
    login_url = "/login/"

    def get_queryset(self):
        return Delivery.objects.filter(
            person_assigned=self.request.user
        ).prefetch_related("destination_warehouses")


class DeliveryCreateView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        context = {
            "users": User.objects.all(),
            "warehouses": Warehouse.objects.all(),
            "profile": self.request.user.profile,
        }
        return render(request, "delivery/create_delivery.html", context)

    def post(self, request):
        pass
