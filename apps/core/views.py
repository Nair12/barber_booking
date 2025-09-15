from multiprocessing.connection import Client

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from apps.core.models import BarbersPoint


def about_view(request):
    return render(request, 'about.html')




def base_view(request):
    return render(request, "pages/base.html")

def home_view(request):
    return render(request, "pages/home.html")



def number_check_view(request):
    return  render(request,"pages/number_check.html")









@require_http_methods(["GET", "POST"])
def bookings(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        date_time = request.POST.get("date_time")
        point_id = request.POST.get("point")


        redirect("mybooking")



    #GET
    context= {
    "points": BarbersPoint.objects.all(),
    }
    return render(request, "pages/booking_create.html",context=context)