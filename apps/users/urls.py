from tkinter.font import names

from django.contrib import admin
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from apps.users.views import barber_create_view, barber_dashboard, admin_dashboard, navigator, admin_create_view

app_name = 'users'

import apps.users.views

urlpatterns = [
     path('register/', apps.users.views.RegisterView.as_view(), name='register'),
     path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logged_out.html'), name='logout'),

    path(route='barber-dashboard/', view=barber_dashboard, name='barber-dashboard'),

    path(route='admin-dashboard/', view=admin_dashboard, name='admin-dashboard'),

    path('barber-create/',barber_create_view, name="barber_create"),

    path('user-create/',apps.users.views.UserAddView.as_view(), name="user_create"),

    path('admin-create/',admin_create_view,name="admin_create"),

    path('navigator/', navigator, name='navigator'),

 ]