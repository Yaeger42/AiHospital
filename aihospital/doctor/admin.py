from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
# Models
from doctor.models import Profile


@admin.register(Profile)
class ProfileDoctorAdmin(admin.ModelAdmin):
    """"Doctor admin profile"""
    list_display = ('pk', 'user', 'specialty', 'cedMed', 'phoneNumber', 'bDay',)
    list_display_links = ('pk', 'user', 'cedMed')
    list_editable = ('phoneNumber', 'specialty',)

    search_fields = ('cedMed', 'user__username', 'user__email', 'specialty',)

    fieldsets = (
        ('Profile', {
            'fields': (('user', 'cedMed'),),
        }),
        ('Extra info', {
            'fields': (('phoneNumber', 'specialty', 'bDay'),),
        }),

    )

    readonly_fields = ('cedMed',)


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
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
