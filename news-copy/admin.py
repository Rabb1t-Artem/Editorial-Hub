from django.contrib import admin

from news.models import Newspaper, Topic


@admin.register(Newspaper)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "redactor"]
    list_filter = ["created_at", "topics", "redactor"]
    search_fields = ["title", "content"]

    def get_topic(self, obj):
        return obj.topic.name if obj.topic else ''
    get_topic.short_description = 'Topic'


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]