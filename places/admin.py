from django.contrib import admin
from places.models import Country, City

admin.site.register(Country, admin.ModelAdmin)
admin.site.register(City, admin.ModelAdmin)
