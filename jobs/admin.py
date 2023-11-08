from django.contrib import admin
from django.contrib.gis import forms

from .models import Comment, EmployeeModel, ExperienceModel, CityModel, CompanyModel


@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'phone_number']
    list_display_links = ['company_name', 'phone_number']
    search_fields = ['company_name', 'phone_number']


@admin.register(CityModel)
class CityModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']


@admin.register(ExperienceModel)
class ExperienceModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']
    list_filter = ['created_at']


@admin.register(EmployeeModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
    list_display_links = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'third_name']
    list_filter = ['created_at']


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    list_display_links = ['name', 'position']
    search_fields = ['name', 'position']
    # readonly_fields = ['user', 'position', 'employ_from', 'employ_to', 'content', 'employee', 'created_at']
    list_filter = ['created_at']
