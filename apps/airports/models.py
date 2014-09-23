from django.contrib.gis.db import models

# Create your models here.
class Airport(models.Model):
    """Represents a US county"""
    name = models.CharField(max_length=60)
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

    def __str__(self):
        return"{}".format(self.name)