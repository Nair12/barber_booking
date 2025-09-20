from tkinter.font import names

from django.contrib import admin
from django.urls import path, include

from apps.core.models import Booking
from apps.core.views import base_view, bookings, number_check_view, home_view, points_view, \
    barber_create_view, booking_success_view, PointDetailsView, point_add_view, BookingDetailsView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view),
    path('booking/', bookings,name="bookings"),
    path('number-check/', number_check_view,name="number_check"),

    path('points/', points_view),

    path('barber-create/', barber_create_view,name="barber_create"),
    path('booking-success/<int:pk>', booking_success_view,name="booking-success"),

    path('point-details/<int:pk>',PointDetailsView.as_view(), name="point-details"),

    path('point-add',point_add_view,name="point_add"),

    path('booking/<int:pk>',BookingDetailsView.as_view(),name="booking-details"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
