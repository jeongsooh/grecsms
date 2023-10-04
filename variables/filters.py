import django_filters
from .models import Variables

class VariablesFilter(django_filters.FilterSet):
  class Meta:
    model = Variables
    fields = {
      'group':['exact'],
      'interval':['exact'],
    }