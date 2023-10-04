from django.contrib import admin
from .models import User, Admin

# Register your models here.

class UserAdmin(admin.ModelAdmin):
  list_display = ('userid', 'name', 'email', 'phone', 'register_dttm', 'last_use_dttm')

admin.site.register(User, UserAdmin)

class AdminAdmin(admin.ModelAdmin):
  list_display = ('userid', 'name', 'email', 'phone', 'register_dttm', 'last_use_dttm')

admin.site.register(Admin, AdminAdmin)
