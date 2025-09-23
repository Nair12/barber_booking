from tkinter.font import names

from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'users'

import apps.users.views

urlpatterns = [
     path('register/', apps.users.views.RegisterView.as_view(), name='register'),
     path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

 ]