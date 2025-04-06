from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, View

from apps.warehouses.models import Warehouse

# Create your views here.


class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse
    template_name = "warehouses/list_warehouses.html"
    context_object_name = "warehouses"
    login_url = "/login/"

    def get_queryset(self):
        return Warehouse.objects.order_by("code")


class WarehouseCreateView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        return render(request, "warehouses/create_warehouse.html")

    def post(self, request):
        code = request.POST.get("code").strip()
        warehouse_name = request.POST.get("warehouse_name").strip()
        warehouse_address = request.POST.get("warehouse_address").strip()
        warehouse_geotag = request.POST.get("warehouse_geotag").strip()

        warehouse_input = {
            "code": code,
            "warehouse_name": warehouse_name,
            "warehouse_address": warehouse_address,
            "warehouse_geotag": warehouse_geotag,
            "actor": request.user,
        }

        # Cek duplicated code (primary key)
        if Warehouse.objects.filter(code=code).exists():
            messages.error(request, "Kode gudang ini sudah digunakan.")
            return render(request, "warehouses/create_warehouse.html", warehouse_input)

        # Cek duplicated name/geotag
        existing_warehouse = Warehouse.objects.filter(
            Q(warehouse_name__istartswith=warehouse_name)
            | Q(warehouse_geotag__istartswith=warehouse_geotag)
        ).first()

        if existing_warehouse:
            if warehouse_name.lower() == existing_warehouse.warehouse_name.lower():
                messages.error(
                    request, "Nama gudang ini sudah terdaftar. Tolong periksa kembali."
                )
            elif warehouse_geotag == existing_warehouse.warehouse_geotag:
                messages.error(
                    request,
                    "Geotag gudang ini sudah terdaftar. Tolong periksa kembali.",
                )

            return render(request, "warehouses/create_warehouse.html", warehouse_input)

        try:
            Warehouse(
                code=code,
                warehouse_name=warehouse_name,
                warehouse_address=warehouse_address,
                warehouse_geotag=warehouse_geotag,
                actor=request.user,
            ).save()

            messages.success(request, "Warehouse successfully created")

            return render(request, "warehouses/create_warehouse.html")

        except IntegrityError as e:
            messages.error(request, f"Error: {e}")

            return render(request, "warehouses/create_warehouse.html", warehouse_input)


class WarehouseUpdateView(LoginRequiredMixin, UpdateView):
    model = Warehouse
    template_name = "warehouses/detail_warehouse.html"
    fields = ["warehouse_name", "warehouse_address", "warehouse_geotag", "code"]
    context_object_name = "warehouse"
    pk_url_kwarg = "id"
    login_url = "/login/"

    def form_valid(self, form):
        messages.success(self.request, "Warehouse updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Failed to update warehouse. Please check the input."
        )
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy("warehouse-list")


class WarehouseDeleteView(LoginRequiredMixin, View):
    login_url = "/login/"

    def post(self, request, id):
        warehouse = Warehouse.objects.get(id=id)
        warehouse.delete()

        return redirect("warehouse-list")
