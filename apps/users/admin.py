from django.contrib import admin

from .models import ProfileUser

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "get_email")

    def get_email(self, obj):
        return obj.user.email

    get_email.short_description = "Email"


admin.site.register(ProfileUser, UserProfileAdmin)
