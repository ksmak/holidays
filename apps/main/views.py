# Django modules
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
# Project modules
from .models import Holiday
from .forms import HolidayForm
from dictionaries.models import Department, Management


class HolidayCreateView(CreateView):
    """ Holiday create view """
    model = Holiday

    form_class = HolidayForm

    success_url = '/detail/{id}'


class HolidayUpdateView(UpdateView):
    """ Holiday update view """
    model = Holiday

    form_class = HolidayForm

    success_url = '/'


class HolidayDetailView(DetailView):
    """ Holiday detail view """
    model = Holiday


class HolidayDeleteView(DeleteView):
    """ Holiday delete view """
    model = Holiday

    success_url = '/'


class HolidayListView(ListView):
    """ Holiday list view """
    model = Holiday

    queryset = Holiday.objects.all()

    context_object_name = 'holidays'

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['departments'] = Department.objects.all()
        context ['managements'] = Management.objects.all()
        return context








