from django.contrib import admin
from django.urls import path, include

from apps.core.views import about_view, base_view, bookings, number_check_view, home_view

urlpatterns = [
    path('', home_view),
    path('booking/', bookings,name="bookings"),
    path('number-check/', number_check_view),
]
