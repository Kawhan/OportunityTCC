from django.contrib import admin
from auth_django.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'auth_provider', 'created_at']
