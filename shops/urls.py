from django.conf.urls import url
from shops.views import ShopList, ShopDetail, ShopEdit, ShopCreate

urlpatterns = [
    url(r'^all/$', ShopList.as_view(), name='all_shops'),
    url(r'^(?P<pk>\d+)/$', ShopDetail.as_view(), name='shop'),
    url(r'^(?P<pk>\d+)/edit$', ShopEdit.as_view(), name='shop_edit'),
    url(r'^add$', ShopCreate.as_view(), name='shop_add'),
]
