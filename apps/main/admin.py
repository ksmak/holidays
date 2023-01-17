# Python modules
from typing import Any
# Django modules
from django.contrib import admin
from django.utils import timezone
# Project modules
from .models import Holiday


class HolidayAdmin(admin.ModelAdmin):
    model = Holiday

    list_display = (
        'number',
        'department',
        'management',
        'last_name',
        'first_name',
        'middle_name'
    )

    add_fieldsets = (
        (None, {
            'fields': (
                'number',
                'department',
                'management',
                'last_name',
                'first_name',
                'middle_name'
            )
        }),
        (None, {
            'fields': (
                'create_date',
                'create_user',
                'change_date',
                'change_user'
            )
        })
    )

    fieldsets = (
        (None, {
            'fields': (
                'number',
                'department',
                'management',
                'last_name',
                'first_name',
                'middle_name'
            )
        }),
        (None, {
            'fields': (
                'create_date',
                'create_user',
                'change_date',
                'change_user'
            )
        })
    )

    search_fields = (
        'number',
    )

    ordering = (
        'number',
    )

    readonly_fields = (
        'create_user',
        'create_date',
        'change_user',
        'change_date'
    )

    list_display_links = (
        'number',
        'department',
        'management',
        'last_name',
        'first_name',
        'middle_name'
    )

    def save_model(
        self,
        request: Any,
        obj: Holiday,
        form: Any,
        change: Any
    ) -> None:
        if not change:
            obj.create_date = timezone.now()
            obj.create_user = request.user
        else:
            obj.change_date = timezone.now()
            obj.change_user = request.user

        return super().save_model(request, obj, form, change)


admin.site.register(Holiday, HolidayAdmin)
