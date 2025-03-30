from os import waitid_result

from django.views.generic import ListView, View
from django.shortcuts import render, redirect

from apps.warehouses.models import Warehouse


# Create your views here.

class WarehouseListView(ListView):
    model = Warehouse
    template_name = 'warehouse_management.html'
    context_object_name = 'warehouses'

class WarehouseCreateView(View):
    def get(self, request):
        return render(request, "detail_warehouse.html")

    def post(self, request):
        warehouse_name = request.POST.get('warehouse_name')
        warehouse_address = request.POST.get('warehouse_address')
        warehouse_geotag = request.POST.get('warehouse_geotag')

        warehouse_input = {"warehouse name": warehouse_name, "warehouse address": warehouse_address, "geotag": warehouse_geotag, "actor": request.user}
        Warehouse(warehouse_name=warehouse_name, warehouse_address=warehouse_address, warehouse_geotag=warehouse_geotag, actor=request.user).save()

        print(warehouse_input)

        return render(request, "detail_warehouse.html", warehouse_input)

class WarehouseDeleteView(View):
    def post(self, request, id):
        warehouse = Warehouse.objects.get(id=id)
        warehouse.delete()

        return redirect('warehouse-list')