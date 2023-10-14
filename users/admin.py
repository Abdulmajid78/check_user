from django.contrib import admin
from .models import CustomUser, EmployeeModel


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


