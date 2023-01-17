# Django modules
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.conf import settings
# Project modules
from .models import Holiday
from .forms import HolidayForm
from dictionaries.models import Department, Management
# Thrid part modules
import os
from docx import Document
import uuid


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


def print_doc(requiest: HttpRequest, pk: int):

    hd = Holiday.objects.get(id=pk)

    doc = Document(os.path.join(settings.UPLOAD_PATH, 'blank.docx'))
    
    file_name = os.path.join(settings.UPLOAD_PATH, str(uuid.uuid4()) + '.docx')

    fields = [f.name for f in Holiday._meta.get_fields()]

    for field in fields:
        for paragraph in doc.paragraphs:
            paragraph.text = paragraph.text.replace(
                f"[{field}]",
                str(getattr(hd, field))
            )

    doc.save(file_name)
    
    return HttpResponse(f"<a href={file_name}>Открыть документ</a>")





