from modeltranslation.translator import translator, TranslationOptions
from .models import (
    Department,
    Management,
    Degree
)
from abstracts.models import AbstractDictionary


class AbstractDictionaryTranslationOptions(TranslationOptions):
    fields = ('title', )


class DepartmentTranslationOptions(TranslationOptions):
    # fields = ('title', )
    pass


class ManagementTranslationOptions(TranslationOptions):
    # fields = ('title', )
    pass


class DegreeTranslationOptions(TranslationOptions):
    # fields = ('title', )
    pass


translator.register(AbstractDictionary, AbstractDictionaryTranslationOptions)
translator.register(Department, DepartmentTranslationOptions)
translator.register(Management, ManagementTranslationOptions)
translator.register(Degree, DegreeTranslationOptions)