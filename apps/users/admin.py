from django.contrib import admin
from .models import ProfileUser

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email')

admin.site.register(ProfileUser, UserProfileAdmin)