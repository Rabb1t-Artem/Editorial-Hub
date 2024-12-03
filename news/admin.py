from django.contrib import admin

from .models import Newspaper, Topic


@admin.register(Newspaper)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "publication_date", "get_topic"]
    list_filter = ["publication_date", "topic", "publishers"]
    search_fields = ["title", "topic__name"]

    def get_topic(self, obj):
        return obj.topic.name if obj.topic else ''
    get_topic.short_description = 'Topic'


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]