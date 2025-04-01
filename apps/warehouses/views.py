from os import waitid_result
from django.contrib import messages

from django.views.generic import ListView, View, UpdateView
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from apps.warehouses.models import Warehouse


# Create your views here.

class WarehouseListView(LoginRequiredMixin, ListView):
    model = Warehouse
    template_name = 'warehouses/list_warehouses.html'
    context_object_name = 'warehouses'
    login_url = '/login/'

class WarehouseCreateView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, "warehouses/create_warehouse.html")

    def post(self, request):
        warehouse_name = request.POST.get('warehouse_name')
        warehouse_address = request.POST.get('warehouse_address')
        warehouse_geotag = request.POST.get('warehouse_geotag')

        warehouse_input = {"warehouse name": warehouse_name, "warehouse address": warehouse_address, "geotag": warehouse_geotag, "actor": request.user}
        Warehouse(warehouse_name=warehouse_name, warehouse_address=warehouse_address, warehouse_geotag=warehouse_geotag, actor=request.user).save()

        messages.success(request, 'Warehouse successfully created')

        return render(request, "warehouses/create_warehouse.html", warehouse_input)

class WarehouseUpdateView(LoginRequiredMixin, UpdateView):
    model = Warehouse
    template_name = "warehouses/detail_warehouse.html"
    fields = ['warehouse_name', 'warehouse_address', 'warehouse_geotag']
    context_object_name = 'warehouse'
    pk_url_kwarg = 'id'
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, "Warehouse updated successfully.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Failed to update warehouse. Please check the input.")
        return self.render_to_response(self.get_context_data(form=form))

    def get_success_url(self):
        return reverse_lazy('warehouse-list')


class WarehouseDeleteView(LoginRequiredMixin, View):
    login_url = '/login/'

    def post(self, request, id):
        warehouse = Warehouse.objects.get(id=id)
        warehouse.delete()

        return redirect('warehouse-list')