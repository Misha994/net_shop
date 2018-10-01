from django.db import models


class ShopType(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Shop(models.Model):
    shop_type = models.ForeignKey('ShopType', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    owner = models.ForeignKey('contacts.Contact', related_name='owner_shops', on_delete=models.CASCADE)
    employee = models.ManyToManyField('contacts.Contact')
    city = models.ForeignKey('places.City', on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    warehouses = models.ManyToManyField('warehouses.Warehouse')
    site = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'shop', (), {'pk': self.pk}
