from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DictionariesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dictionaries'
    verbose_name = _('справочники')
