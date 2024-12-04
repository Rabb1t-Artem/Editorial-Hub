from django.contrib import admin

from .models import Newspaper, Topic


@admin.register(Newspaper)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "redactor"]
    list_filter = ["created_at", "topics", "redactor"]
    search_fields = ["title", "content"]
    filter_horizontal = ["topics"]


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]