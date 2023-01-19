from django.db import models


class Department(models.Model):
    """ Department model """
    title = models.CharField(
        verbose_name='наименование',
        max_length=150
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'подразделение',
        verbose_name_plural = 'подразделения'
        ordering = (
            'title',
        )


class Management(models.Model):
    """ Management model """
    title = models.CharField(
        verbose_name='наименование',
        max_length=150
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'служба',
        verbose_name_plural = 'службы'
        ordering = (
            'title',
        )


class Degree(models.Model):
    """ Degree model """
    title = models.CharField(
        verbose_name='наименование',
        max_length=150
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'звание',
        verbose_name_plural = 'звания'
        ordering = (
            'title',
        )
