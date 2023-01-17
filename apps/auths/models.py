# Django modules
from django.db import models
from django.contrib.auth.models import AbstractUser
# Project modules
from dictionaries.models import Department, Management


class CustomUser(AbstractUser):
    """ Custom user model """
    middle_name = models.CharField(
        verbose_name='отчество',
        max_length=150,
        null=True,
        blank=True
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

    def __str__(self) -> str:
        return f"{self.username}"
