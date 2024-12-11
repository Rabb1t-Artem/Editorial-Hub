from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Redactor


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("years_of_experience",)
    list_filter = UserAdmin.list_filter + ("years_of_experience",)
    search_fields = ("first_name", "last_name")

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
