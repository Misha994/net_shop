from django.conf.urls import url
from warehouses.views import WarehouseCreate, WarehouseDetail, WarehouseEdit, WarehouseList

urlpatterns = [
    url(r'^all/$', WarehouseList.as_view(), name='all_warehouses'),
    url(r'^(?P<pk>\d+)/$', WarehouseDetail.as_view(), name='warehouse'),
    url(r'^(?P<pk>\d+)/edit$', WarehouseEdit, name='warehouse_edit'),
    url(r'^add$', WarehouseCreate.as_view(), name='warehouse_add'),
]
