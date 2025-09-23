from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from apps.users.forms import CustomUserCreationForm


class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('user:login')



