# Project modules
from abstracts.models import AbstractDictionary
from django.utils.translation import gettext_lazy as _


class Department(AbstractDictionary):
    """ Department model """
   
    class Meta:
        verbose_name = _('подразделение'),
        verbose_name_plural = _('подразделения')
        ordering = (
            'title',
        )


class Management(AbstractDictionary):
    """ Management model """
    
    class Meta:
        verbose_name = _('служба'),
        verbose_name_plural = _('службы')
        ordering = (
            'title',
        )


class Degree(AbstractDictionary):
    """ Degree model """
    
    class Meta:
        verbose_name = _('звание'),
        verbose_name_plural = _('звания')
        ordering = (
            'title',
        )
