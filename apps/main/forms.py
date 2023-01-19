# Django modules
from django import forms
# Project modules
from .models import Holiday
from dictionaries.models import Department, Management


class HolidayForm(forms.ModelForm):
    """ Holiday form """
    date_enter = forms.DateField(
        label='Берілген күні',
        widget=forms.widgets.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}
        )
    )

    date_start = forms.DateField(
        label='Басталу күні',
        widget=forms.widgets.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}
        )
    )

    date_end = forms.DateField(
        label='Аяқталу күні',
        widget=forms.widgets.DateInput(
            format=('%Y-%m-%d'),
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Holiday

        fields = (
            'number',
            'date_enter',
            'date_start',
            'date_end',
            'department',
            'management',
            'last_name',
            'first_name',
            'middle_name',
            'degree',
            'job',
            'place'
        )
        
        labels = {
            'number': 'Нөмір',
            'date_enter': 'Берілген күні',
            'date_start': 'Басталу күні',
            'date_end': 'Аяқталу күні',
            'department': 'Бөлім',
            'management': 'Қызмет',
            'last_name': 'Тегі',
            'first_name': 'Аты',
            'middle_name': 'Әкесінің аты',
            'degree': 'Атағы',
            'job': 'Лауазым',
            'place': 'Баратын жері'
        }