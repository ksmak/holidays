# Django modules
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Project modules
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser

    fieldsets = (
        ('Персональные данные', {
            'classes': (
                'wide',
            ),
            'fields':  (
                'username',
                'first_name',
                'last_name',
                'middle_name',
                'department',
                'management',
                'email',
                'password',
            )
        }),
        ('Служебные данные', {
            'classes': (
                'wide',
            ),
            'fields':
            (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        })
    )

    add_fieldsets = (
        ('Персональные данные', {
            'classes': (
                'wide',
            ),
            'fields':  (
                'username',
                'first_name',
                'last_name',
                'middle_name',
                'department',
                'management',
                'email',
                'password1',
                'password2'
            )
        }),
        ('Служебные данные', {
            'classes': (
                'wide',
            ),
            'fields':
            (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        })
    )

    list_display = (
        'username',
        'last_name',
        'first_name',
        'middle_name',
        'department',
        'management',
        'is_active'
    )

    search_fields = (
        'username',
        'last_name',
        'first_name',
        'middle_name'
    )

    ordering = (
        'username',
        'last_name',
        'first_name',
        'middle_name'
    )

    list_display_links = (
        'username',
        'last_name',
        'first_name',
        'middle_name'
    )


admin.site.register(CustomUser, CustomUserAdmin)
