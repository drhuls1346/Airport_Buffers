from apps.airports import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class AirportSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Airport
        geo_field = 'geom'
        fields = ('id','name')
