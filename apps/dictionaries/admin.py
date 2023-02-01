from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (
    Department,
    Management,
    Degree
)


class DepartmentAdmin(TranslationAdmin):
    pass

   
class ManagementAdmin(TranslationAdmin):
    pass

   
class DegreeAdmin(TranslationAdmin):
    pass

    
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Degree, DegreeAdmin)
