from django import forms

from apps.core.models import Booking, Barber


class BookingForm(forms.Form):
    class Meta:
        model = Booking
        fields = ['name','number','datetime']
        widgets = {


        }



class BarberForm(forms.Form):
    class Meta:
        model = Barber
        fields = "__all__"
        exclude = ["user"]