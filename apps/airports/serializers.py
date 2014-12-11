from apps.airports import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class AirportSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Airports
        geo_field = 'geom'
        fields = ('name', 'city', 'faa')

class CampusesSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Campuses
        geo_field = 'geom'
        fields = ('name')