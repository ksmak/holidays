# Django modules
from django.urls import path

# Project modules
from .views import (
    HolidayCreateView,
    HolidayUpdateView,
    HolidayDetailView,
    HolidayDeleteView,
    HolidayListView,
    print_doc
)


urlpatterns = [
    path('', HolidayListView.as_view(), name='list'),
    path('create/', HolidayCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', HolidayUpdateView.as_view(), name='edit'),
    path('detail/<int:pk>/', HolidayDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', HolidayDeleteView.as_view(), name='delete'),
    path('print/<int:pk>/', print_doc, name='print'),
]
