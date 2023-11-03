from django.contrib import admin
from .models import CompanyUser, Profile


@admin.register(CompanyUser)
class CompanyUserAdmin(admin.ModelAdmin):
    list_display = ['company_name']
    list_display_links = ['company_name']
    search_fields = ['company_name']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name']
    list_display_links = ['user', 'company_name']
    search_fields = ['company_name']
    raw_id_fields = ['user']









