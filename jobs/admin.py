from django.contrib import admin

from .models import CommentModel


@admin.register(CommentModel)
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
