from django.contrib import admin
from .models import Tenant

# Register your models here.
@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_details', 'property', 'section_occupied']
    search_fields = ['name', 'contact_details']
