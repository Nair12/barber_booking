from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View, generic

from apps.core.models import Barber, Booking, Admin, BarbersPoint
from apps.users.forms import CustomUserCreationForm
from apps.users.models import CustomUser


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')


class UserAddView(generic.FormView):
    login_url = reverse_lazy('users:login')
    template_name = "users/add-user.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:admin-dashboard')

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)





def navigator(request):
    if request.user.role == 'barber':
        return redirect('/workspace/barber-dashboard/')
    elif request.user.role == 'admin':
        return redirect('/workspace/admin-dashboard/')
    else:
        return redirect('/workspace/register/')



@login_required(login_url='users:login')
def barber_dashboard(request):
    barber = Barber.objects.get(user=request.user)
    bookings = Booking.objects.filter(barber=barber)
    context = {
        'barber': barber,
        'bookings': bookings
    }
    return render(request,'users/barber-dashboard.html', context)



@login_required(login_url=' users:login')
def admin_dashboard(request):
    admin = Admin.objects.get(user=request.user)
    barbers = Barber.objects.all()
    admins = Admin.objects.all()
    points = BarbersPoint.objects.all()
    context = {
        'admins': admins,
        'barbers': barbers,
        'points': points,
    }

    return render(request, 'users/admin-dashboard.html',context)


@login_required(login_url='users:login')
def barber_create_view(request):
    if request.method == "POST":
        phone = request.POST["phone"]
        exp = request.POST["exp"]
        salary = request.POST["salary"]
        picture = request.FILES["picture"]
        point_id = request.POST["point"]
        user_login = request.POST["user-login"]

        user = CustomUser.objects.get(username=user_login)
        user.role = 'barber'
        user.save()

        new_object = Barber.objects.create(phone=phone, exp=exp,
                               salary=salary,
                              pict_url=picture,point_id=point_id,user=user)
        print(new_object)
        return redirect("/")

    context = {
        "points": BarbersPoint.objects.all(),
    }
    print("Context:".format(context))

    return render(request,"users/barber_create.html",context=context)



@login_required(login_url='users:login')
def admin_create_view(request):
    if request.method == "POST":
        patronymic = request.POST["patronymic"]
        user_login = request.POST["user-login"]

        user = CustomUser.objects.get(username=user_login)
        user.role = 'admin'
        user.save()
        Admin.objects.create(user=user,patronymic=patronymic)
        return redirect("users:admin-dashboard")


    return render(request,"users/admin-add.html")




