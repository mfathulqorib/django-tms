from os import waitid_result

from django.views.generic import ListView, View
from django.shortcuts import render

from apps.warehouses.models import Warehouse


# Create your views here.

class WarehouseListView(ListView):
    model = Warehouse
    template_name = 'warehouse_management.html'
    context_object_name = 'warehouses'

class WarehouseCreateView(View):
    def get(self, request):
        return render(request, "create_warehouses.html")

    def post(self, request):
        warehouse_name = request.POST.get('warehouse_name')
        warehouse_address = request.POST.get('warehouse_address')
        warehouse_geotag = request.POST.get('warehouse_geotag')

        warehouse_input = {"warehouse name": warehouse_name, "warehouse address": warehouse_address, "geotag": geotag, "actor": request.user}
        Warehouse(warehouse_name=warehouse_name, warehouse_address=warehouse_address, geotag=geotag, actor=request.user).save()

        print(warehouse_input)

        return render(request, "create_warehouses.html", warehouse_input)