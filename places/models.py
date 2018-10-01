from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'all_places', ()


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return 'place_edit', (), {'pk': self.pk}
