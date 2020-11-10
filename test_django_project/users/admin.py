from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from users.models import User


class CustomUserAdmin(UserAdmin):
    ordering = ('id',)
    list_display = ('id', 'username', 'first_name', 'last_name', 'email',
                    'phone_number', 'is_active', 'is_staff')
    list_display_links = ('id', 'username', 'first_name', 'last_name', 'email')
    list_filter = ('is_staff',)

    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'nickname')}),
        ('Personal info', {'fields': ('avatar', 'first_name', 'last_name', 'phone_number')}),
        ('User Details', {'fields': ('is_active', 'is_staff')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name',
                       'phone_number', 'password1', 'password2'),
        }),
    )


admin.site.register(User, CustomUserAdmin)
