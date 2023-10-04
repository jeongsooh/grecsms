from django.contrib import admin
from .models import Cpconfig

# Register your models here.

class CpconfigAdmin(admin.ModelAdmin):
  list_display = ('cpnumber', 'cpserial', 'register_dttm',)

admin.site.register(Cpconfig, CpconfigAdmin)
