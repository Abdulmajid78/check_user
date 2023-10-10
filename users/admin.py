from django.contrib import admin

from .models import EmployeeModel


@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'is_active']
    list_display_links = ['id', 'first_name']

