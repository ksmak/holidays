# Python modules
import datetime
from typing import Any, Optional, Union
# Django modules
from django.shortcuts import render
from django.http import (
    HttpRequest,
    HttpResponse,
    Http404,
    HttpResponseRedirect
)
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)
from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.db.models import Q
from django.core.paginator import (
    Paginator,
    PageNotAnInteger,
    EmptyPage
)
# Project modules
from .models import Holiday
from .forms import HolidayForm
from dictionaries.models import Department, Management
# Thrid part modules
import os
from docx import Document
import uuid


class HolidayCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    CreateView
):
    """ Holiday create view """
    model = Holiday

    form_class = HolidayForm

    success_url = '/detail/{id}'

    def form_valid(self, form):
        form.instance.create_user = self.request.user
        form.instance.create_date = timezone.now()
        return super().form_valid(form)

    permission_required = 'main.add_holiday'

class HolidayUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UpdateView
):
    """ Holiday update view """
    model = Holiday

    form_class = HolidayForm

    success_url = '/detail/{id}'

    def form_valid(self, form):
        form.instance.change_user = self.request.user
        form.instance.change_date = timezone.now()
        return super().form_valid(form)

    permission_required = 'main.change_holiday'

class HolidayDetailView(LoginRequiredMixin, DetailView):
    """ Holiday detail view """
    model = Holiday


class HolidayDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DeleteView
):
    """ Holiday delete view """
    model = Holiday

    success_url = '/'

    permission_required = 'main.delete_holiday'


class HolidayPaginator(Paginator):
    """ Holiday custom paginator """
    def validate_number(
        self,
        number: Optional[Union[int, float, str]]
    ) -> int:
        try:
            return super().validate_number(number)
        except PageNotAnInteger:
            return super().validate_number(1)
        except EmptyPage:
            return super().validate_number(1)


class HolidayListView(LoginRequiredMixin, ListView):
    """ Holiday list view """
    model = Holiday

    paginate_by = 200

    paginator_class = HolidayPaginator

    def get_queryset(self) -> QuerySet[Any]:

        ft_name: str = self.request.GET.get('ft_name', '')
        ft_department: str = self.request.GET.get('ft_department', '')
        ft_management: str = self.request.GET.get('ft_management', '')
        
        q: QuerySet = Holiday.objects.all()

        if ft_name:
            q1: Q = Q(first_name__istartswith=ft_name)
            q2: Q = Q(last_name__istartswith=ft_name)
            q3: Q = Q(middle_name__istartswith=ft_name)

            q = q.filter(q1 | q2 | q3)
        
        if ft_department:
            q = q.filter(department_id=int(ft_department))

        if ft_management:
            q = q.filter(management_id=int(ft_management))
        
        return q.order_by(self.get_ordering())

    context_object_name = 'holidays'

    def get_context_data (self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Department.objects.all()
        context['managements'] = Management.objects.all()
        context['order_by'] = self.request.GET.get('order_by', 'number')
        context['ft_name'] = self.request.GET.get('ft_name', '')
        context['ft_department'] = self.request.GET.get('ft_department')
        context['ft_management'] = self.request.GET.get('ft_management')
        context['page'] = self.request.GET.get('page', 1)
        return context

    def get_ordering(self):
        ordering = self.request.GET.get('order_by', 'number')
        return ordering


@login_required
def print_doc(requiest: HttpRequest, pk: int):
    """ 
        the method outputs data to the Word 
        using the module python-docx
    """

    hd = Holiday.objects.get(id=pk)

    doc = Document(os.path.join(settings.MEDIA_ROOT, 'blank.docx'))
    
    file_path = os.path.join(settings.MEDIA_ROOT, str(uuid.uuid4()) + '.docx')

    fields = [f.name for f in Holiday._meta.get_fields()]

    fields.sort(key=len)
    
    fields.reverse()

    for field in fields:

        val = getattr(hd, field)

        if type(val) == datetime.date:
            val = val.strftime("%d.%m.%Y")
        else:
            val = str(val)
        
        for paragraph in doc.paragraphs:
            if f"{field}" in paragraph.text:
                for run in paragraph.runs:
                    if f"{field}" in run.text:
                        run.text = run.text.replace(f"{field}", val)
                        run.bold = True

    doc.save(file_path)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        
        os.remove(file_path)
        
        return response
    
    raise Http404

