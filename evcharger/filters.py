import django_filters
from .models import Evcharger

class EvchargerFilter(django_filters.FilterSet):
  class Meta:
    model = Evcharger
    fields = '__all__'
    exclude = ['cpnumber', 'cpsite', 'cpstatus', 'register_dttm',]