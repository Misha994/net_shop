from django.shortcuts import redirect, render
from django.contrib import messages
from warehouses.models import Warehouse
from django.views.generic import ListView, DetailView, CreateView
from warehouses.forms import WarehouseForm


class WarehouseList(ListView):
    model = Warehouse
    context_object_name = 'warehouses'
    template_name = 'warehouses/all_warehouses.html'


class WarehouseDetail(DetailView):
    model = Warehouse
    context_object_name = 'warehouse'
    template_name = 'warehouses/warehouse_detail.html'


class WarehouseCreate(CreateView):
    model = Warehouse
    fields = '__all__'
    template_name = 'warehouses/warehouse_form.html'


def WarehouseEdit(request, pk):
    form = WarehouseForm(request.POST or None, instance=Warehouse.objects.get(pk=pk))
    if form.is_valid():
        warehouse = form.save()
        messages.success(request, 'success')
        return redirect('warehouse_edit', pk=warehouse.pk)
    return render(request, 'warehouses/warehouse_form.html', {'form': form})
