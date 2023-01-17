# Django modules
from django import forms
# Project modules
from .models import Holiday
from dictionaries.models import Department, Management


class HolidayForm(forms.ModelForm):
    """ Holiday form """
    class Meta:
        model = Holiday
        fields = (
            'number',
            'department',
            'management',
            'last_name',
            'first_name',
            'middle_name'
        )
        labels = {
            'number': 'Номер',
            'department': 'Подразделение',
            'management': 'Служба',
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'middle_name': 'Отчество'
        }