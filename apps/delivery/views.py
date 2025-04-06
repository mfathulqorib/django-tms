from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View
from django.contrib import messages

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
        # Ambil data dari form
        person_assigned_id = request.POST.get("person_assigned")
        eta = request.POST.get("estimated_time_arrival")
        delivery_notes = request.POST.get("delivery_notes")
        warehouse_ids = request.POST.getlist("destination_warehouses")

        # Validasi input
        errors = []
        if not person_assigned_id:
            errors.append("Petugas pengiriman harus dipilih.")
        if not eta:
            errors.append("ETA harus diisi.")
        if not warehouse_ids:
            errors.append("Minimal satu tujuan gudang harus dipilih.")

        if errors:
            # Kirim ulang form dengan input sebelumnya
            context = self.get_context_data(request)
            context.update({
                "input": {
                    "person_assigned": person_assigned_id,
                    "estimated_time_arrival": eta,
                    "delivery_notes": delivery_notes,
                    "destination_warehouses": warehouse_ids,
                },
                "errors": errors,
            })
            return render(request, "delivery/create_delivery.html", context)

        person_assigned = get_object_or_404(User, id=person_assigned_id)
        delivery = Delivery.objects.create(
            actor=self.request.user,
            person_assigned=person_assigned,
            estimated_time_arrival=eta,
            delivery_notes=delivery_notes or ""
        )
        delivery.destination_warehouses.set(warehouse_ids)

        # Pesan sukses dan redirect
        messages.success(request, "Delivery order berhasil dibuat.")

        return redirect(request.path)

    def get_context_data(self, request):
        return {
            "users": User.objects.all(),
            "warehouses": Warehouse.objects.all(),
            "profile": request.user.profile,
        }
