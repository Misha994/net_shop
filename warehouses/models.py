from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey('places.City', on_delete=models.CASCADE)
    address = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'warehouse', (), {'pk': self.pk}
