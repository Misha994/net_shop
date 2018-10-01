from django.contrib import admin
from shops.models import Shop, ShopType

admin.site.register(Shop, admin.ModelAdmin)
admin.site.register(ShopType, admin.ModelAdmin)
