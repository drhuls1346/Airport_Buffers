from apps.airports import models, serializers
from rest_framework import generics
import django_filters

class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type):integers})
        return qs

class CountyFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')
    class Meta:
        model = models.Airport
        fields = ['id', 'name']

class AirportCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Airport.objects.all()
    serializer_class = serializers.AirportSerializer
    filter_class = CountyFilter