# Register your models here.
from accounts.models import User, UserProfile
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .forms import UserProfileForm, UserProfileFormAdmin


class UserProfileInline(admin.StackedInline):
    form = UserProfileFormAdmin
    model = UserProfile
    can_delete = False


class UserAdmin(AuthUserAdmin):
    list_display = ['username', 'email',
                    'auth_provider', 'created_at', 'is_staff', 'verify_staff_user', 'user_is_teacher']

    list_editable = ['is_staff', 'verify_staff_user', 'user_is_teacher']

    def add_view(self, *args, **kwargs):
        self.inlines = []
        return super(UserAdmin, self).add_view(*args, **kwargs)

    def change_view(self, *args, **kwargs):
        self.inlines = [UserProfileInline]
        return super(UserAdmin, self).change_view(*args, **kwargs)


admin.site.register(User, UserAdmin)
