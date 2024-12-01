from django.contrib import admin

from .models import Newspaper, Topic


@admin.register(Newspaper)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "publication_date", "topic"]
    list_filter = ["publication_date", "topic", "publishers"]
    search_fields = ["title", "topic__name"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]