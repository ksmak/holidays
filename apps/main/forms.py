# Django modules
from django import forms
# Project modules
from .models import Holiday
from dictionaries.models import Department, Management


class HolidayForm(forms.ModelForm):
    """ Holiday form """
    class Meta:
        model = Holiday

        fields = ('__all__')

        exclude = (
            'create_date',
            'create_user',
            'change_date',
            'change_user',
        )

        widgets = {
            'date_enter': forms.widgets.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            ),
            'date_start': forms.widgets.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            ),
            'date_end': forms.widgets.DateInput(
                format='%Y-%m-%d',
                attrs={'type': 'date'}
            ),
        }