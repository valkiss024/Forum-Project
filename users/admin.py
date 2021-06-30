from django.contrib import admin

from users.models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """Add the user's staff status to the admin display"""
    list_display = ["username", "is_staff"]


admin.site.register(CustomUser, CustomUserAdmin)
