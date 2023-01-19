# Django modules
from django.db import models
from django.utils import timezone
# Project modules
from auths.models import CustomUser
from dictionaries.models import (
    Department,
    Management,
    Degree
)


class Holiday(models.Model):
    """ Holiday model """
    number = models.IntegerField(
        verbose_name='номер'
    )

    date_enter = models.DateField(
        verbose_name='дата выдачи',
        default=timezone.now
    )

    date_start = models.DateField(
        verbose_name='дата начало',
        default=timezone.now
    )

    date_end = models.DateField(
        verbose_name='дата конец',
        default=timezone.now
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

    job = models.CharField(
        verbose_name='должность',
        max_length=150
    )

    degree = models.ForeignKey(
        to=Degree,
        on_delete=models.RESTRICT,
        verbose_name='звание',
        null=True,
        blank=True
    )

    place = models.CharField(
        verbose_name='место выезда',
        max_length=300,
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
        return f"Отпуск: №{self.number} от {self.date_enter}"

    def save(self, *args, **kwargs):
        if self.first_name:
            self.first_name = self.first_name.capitalize()
        
        if self.last_name:
            self.last_name = self.last_name.capitalize()
        
        if self.middle_name:
            self.middle_name = self.middle_name.capitalize()
        
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'отпуск'
        verbose_name_plural = 'отпуска'
        ordering = (
            'number',
            'date_enter'
        )
