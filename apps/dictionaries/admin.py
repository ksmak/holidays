from django.contrib import admin
from .models import (
    Department,
    Management,
    Degree
)


class DepartmentAdmin(admin.ModelAdmin):
    model = Department

    list_display = (
        'title',
    )

    add_fieldsets = (
        (None, {
            'fields': (
                'title',
            )
        }),
    )

    fieldsets = (
        (None, {
            'fields': (
                'title',
            )
        }),
    )

    search_fields = (
        'title',
    )

    ordering = (
        'title',
    )


class ManagementAdmin(admin.ModelAdmin):
    model = Management

    list_display = (
        'title',
    )

    add_fieldsets = (
        (None, {
            'fields': (
                'title',
            )
        }),
    )

    fieldsets = (
        (None, {
            'fields': (
                'title',
            )
        }),
    )

    search_fields = (
        'title',
    )

    ordering = (
        'title',
    )


class DegreeAdmin(admin.ModelAdmin):
    model = Degree

    list_display = (
        'title',
    )

    add_fieldsets = (
        (None, {
            'fields': (
                'title',
            )
        }),
    )

    fieldsets = (
        (None, {
            'fields': (
                'title',
            )
        }),
    )

    search_fields = (
        'title',
    )

    ordering = (
        'title',
    )


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Degree, DegreeAdmin)
