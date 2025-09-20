from multiprocessing.connection import Client

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404

from apps.core.models import BarbersPoint, Barber, Booking, PointImages



def base_view(request):
    return render(request, "pages/base.html")

def home_view(request):
    return render(request, "pages/home.html")



def number_check_view(request):
    if request.method == "POST":
        number = request.POST.get("number")
        booking = Booking.objects.filter(user_phone=number).first()
        print(booking)
        if booking is not None:
            return redirect("booking-details",pk=booking.id)
        else:
            context = {
                "error_message":"Your booking does not exist,please check phone number",
            }
            return render(request, "pages/number_check.html", context)



    return  render(request,"pages/number_check.html")



def points_view(request):

    context = {
        "points": BarbersPoint.objects.all()
    }
    print(context)


    return render(request,"pages/points.html",context=context)


def barber_create_view(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        exp = request.POST["exp"]
        surname = request.POST["surname"]
        patronymic = request.POST["patronymic"]
        salary = request.POST["salary"]
        picture = request.FILES["picture"]
        point_id = request.POST["point"]
        new_object = Barber.objects.create(name=name, phone=phone, exp=exp,
                              surname=surname, salary=salary,
                              patronymic=patronymic,pict_url=picture,point_id=point_id)
        print(new_object)
        return redirect("/")

    context = {
        "points": BarbersPoint.objects.all(),
    }
    print("Context:".format(context))

    return render(request,"pages/barber_create.html",context=context)



@require_http_methods(["GET", "POST"])
def bookings(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        date_time = request.POST.get("date_time")
        point_id = request.POST.get("point")
        barber_id = 1

        barber = Barber.objects.get(id=barber_id)
        point = BarbersPoint.objects.get(id=point_id)


        new_object = Booking.objects.create(name=name, user_phone=phone, date_time=date_time,point=point,barber=barber)

        return redirect("booking-success",pk=new_object.id)



    #GET
    context= {
    "points": BarbersPoint.objects.all(),
    }
    return render(request, "pages/booking_create.html",context=context)



def booking_success_view(request,pk):
    context={
        "Id":pk
    }

    return render(request, "pages/booking_success.html",context=context)


def point_add_view(request):
    if request.method == "POST":
        address = request.POST["address"]
        phone = request.POST["phone"]
        images = request.FILES.getlist("images")

        new_point = BarbersPoint.objects.create(address=address, phone_number=phone)

        for image in images:
            PointImages.objects.create(image=image,point_id=new_point)
            print(image)

        return redirect("/")



    return render(request, "pages/point_add.html")




class PointDetailsView(View):
    model = BarbersPoint
    def get(self, request,pk):
        point = get_object_or_404(BarbersPoint,id=pk)
        images = PointImages.objects.filter(point_id = pk)
        context = {
            "point": point,
            "images": images,
        }
        print(images)
        return render(request,"pages/point_details.html",context=context)




class BookingDetailsView(View):
    model = Booking
    def get(self, request,pk):
        booking = get_object_or_404(Booking, pk=pk)
        context = {
            "booking": booking,
        }
        print(booking.date_time)
        return render(request,"pages/booking_details.html",context=context)
