from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import UserProfile



admin.site.unregister(User)
admin.site.register(User, UserAdmin)



@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'contact', 'choose']
