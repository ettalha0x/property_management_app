from django.contrib import admin
from .models import Property

# Register your models here.
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'property_type', 'number_of_units', 'rental_cost']
    search_fields = ['name', 'address']
