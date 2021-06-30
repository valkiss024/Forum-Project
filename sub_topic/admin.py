from django.contrib import admin

from sub_topic.models import SubTopic


class SubTopicAdmin(admin.ModelAdmin):
    """Add the author and the date the sub topic was created to the admin display"""
    list_display = ["title", "date", "author"]


admin.site.register(SubTopic, SubTopicAdmin)
