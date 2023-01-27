# Django modules
from django.db import models
from django.utils.translation import gettext_lazy as _


class AbstractDictionary(models.Model):
    """ Abstract Dictionary model """

    title = models.CharField(
        verbose_name=_('наименование'),
        max_length=150
    )

    def __str__(self) -> str:
        return self.title
    

class AbstractModel(models.Model):
    """ Abstract Model """

    create_date = models.DateTimeField(
        verbose_name=_('создан'),
        null=True
    )

    create_user = models.CharField(
        verbose_name=_('кем создан'),
        max_length=150,
        null=True,
        blank=True
    )

    change_date = models.DateTimeField(
        verbose_name=_('изменен'),
        null=True
    )

    change_user = models.CharField(
        verbose_name=_('кем изменен'),
        max_length=150,
        null=True,
        blank=True
    )