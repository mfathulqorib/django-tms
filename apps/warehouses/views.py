from django.views.generic import ListView
from django.shortcuts import render

from apps.warehouses.models import Warehouse


# Create your views here.

class WarehouseListView(ListView):
    model = Warehouse
    template_name = 'warehouse_management.html'
    context_object_name = 'warehouses'
