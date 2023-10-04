from django.contrib import admin
from .models import Evcharger

# Register your models here.

class EvchargerAdmin(admin.ModelAdmin):
  list_display = ('cpnumber', 'cpsite', 'partner_id', 'manager_id', 'public_use', 'cpstatus', 'address', 'cpmodel', 'cpmaker', 'fwversion', 'register_dttm', 'last_modified_dttm')

admin.site.register(Evcharger, EvchargerAdmin)
