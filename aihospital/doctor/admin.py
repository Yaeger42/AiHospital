from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from doctor.models import Profile


@admin.register(Profile)
class ProfileDoctorAdmin(admin.ModelAdmin):
    """"Doctor admin profile"""
    list_display = ('pk', 'user', 'phoneNumber', 'specialty', 'cedID', 'bday')
    list_display_links = ('pk', 'user', 'cedID')
    list_editable = ('phoneNumber', 'specialty')

    search_fields = ('cedID', 'user__username', 'user__email', 'specialty')


class ProfileDoctorAdminInLine(admin.StackedInline):
    """Add profile user admin to base user admin"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileDoctorAdminInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, ProfileDoctorAdmin)
