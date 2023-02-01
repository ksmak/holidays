# Django modules
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Project modules
from abstracts.models import AbstractModel
from dictionaries.models import (
    Department,
    Management,
    Degree
)


class Holiday(AbstractModel):
    """ Holiday model """
    number = models.IntegerField(
        verbose_name=_('номер')
    )

    date_enter = models.DateField(
        verbose_name=_('дата выдачи'),
        default=timezone.now
    )

    date_start = models.DateField(
        verbose_name=_('дата начало'),
        default=timezone.now
    )

    date_end = models.DateField(
        verbose_name=_('дата конец'),
        default=timezone.now
    )

    last_name = models.CharField(
        verbose_name=_('фамилия'),
        max_length=150
    )

    first_name = models.CharField(
        verbose_name=_('имя'),
        max_length=150
    )

    middle_name = models.CharField(
        verbose_name=_('отчество'),
        max_length=150
    )

    department = models.ForeignKey(
        to=Department,
        on_delete=models.RESTRICT,
        verbose_name=_('подразделение'),
        null=True,
        blank=True
    )

    management = models.ForeignKey(
        to=Management,
        on_delete=models.RESTRICT,
        verbose_name=_('служба'),
        null=True,
        blank=True
    )

    job = models.CharField(
        verbose_name=_('должность'),
        max_length=150
    )

    degree = models.ForeignKey(
        to=Degree,
        on_delete=models.RESTRICT,
        verbose_name=_('звание'),
        null=True,
        blank=True
    )

    place = models.CharField(
        verbose_name=_('место выезда'),
        max_length=300,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"№{self.number} - {self.date_enter}"
    
    def clean(self) -> None:
        if self.date_start > self.date_end:
            raise ValidationError(_('дата начала должно быть меньше даты конца'))

    def save(self, *args, **kwargs):
        self.full_clean()

        if self.first_name:
            self.first_name = self.first_name.capitalize()

        if self.last_name:
            self.last_name = self.last_name.capitalize()

        if self.middle_name:
            self.middle_name = self.middle_name.capitalize()

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('отпускное удостоверение')
        verbose_name_plural = _('отпускные удостоверения')
        ordering = (
            'date_enter',
            'number',
        )
