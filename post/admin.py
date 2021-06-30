from django.contrib import admin

from post.models import Post


class PostAdmin(admin.ModelAdmin):
    """Add the sub topic, author and the date the post was created to the admin display"""
    list_display = ["title", "sub_topic", "date", "author"]


admin.site.register(Post, PostAdmin)
