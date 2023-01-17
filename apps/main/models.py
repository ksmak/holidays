# Python modules
# from typing import Optional, Iterable
# Django modules
from django.db import models
# Project modules
from auths.models import CustomUser
from dictionaries.models import (
    Department,
    Management
)


class HolidayManager(models.Manager):
    """ Holiday manager """
    ...


class Holiday(models.Model):
    """ Holiday model """
    number = models.IntegerField(
        verbose_name='номер'
    )

    first_name = models.CharField(
        verbose_name='имя',
        max_length=150
    )

    last_name = models.CharField(
        verbose_name='фамилия',
        max_length=150
    )

    middle_name = models.CharField(
        verbose_name='отчество',
        max_length=150
    )

    department = models.ForeignKey(
        to=Department,
        on_delete=models.RESTRICT,
        verbose_name='подразделение',
        null=True,
        blank=True
    )

    management = models.ForeignKey(
        to=Management,
        on_delete=models.RESTRICT,
        verbose_name='служба',
        null=True,
        blank=True
    )

    create_date = models.DateTimeField(
        verbose_name='создан',
        null=True
    )

    create_user = models.ForeignKey(
        verbose_name='кем создан',
        to=CustomUser,
        on_delete=models.RESTRICT,
        related_name='create_user',
        null=True
    )

    change_date = models.DateTimeField(
        verbose_name='изменен',
        null=True
    )

    change_user = models.ForeignKey(
        verbose_name='кем изменен',
        to=CustomUser,
        on_delete=models.RESTRICT,
        related_name='change_user',
        null=True
    )

    def __str__(self) -> str:
        return f"Отпуск: №{self.number}"

    class Meta:
        verbose_name = 'отпуск'
        verbose_name_plural = 'отпуска'
        ordering = (
            'number',
        )
