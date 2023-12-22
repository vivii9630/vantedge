from django.contrib import admin
from .models import Vehicle, Users

class VehicleInline(admin.TabularInline):
    model = Vehicle
    extra = 0

class UsersAdmin(admin.ModelAdmin):
    inlines = [VehicleInline]

admin.site.register(Users, UsersAdmin)
admin.site.register(Vehicle)


"""class VehicleInline(admin.TabularInline):
   model = Vehicle
   extra=1

class UserAdmin(admin.ModelAdmin):
   list_display = ['username', 'first_name','last_name']
   inlines=[VehicleInline]"""

