from django.contrib import admin

from main_topic.models import MainTopic


class MainTopicAdmin(admin.ModelAdmin):
    """Add the date the topic was created to the admin display"""
    list_display = ["title", "date"]


admin.site.register(MainTopic, MainTopicAdmin)
