from django.shortcuts import redirect
from django.urls import resolve


EXEMPT_URLS = [
    'welcome',
    'register',
    'login',
    'logout',
    'logged_out',
    'booking-details',
    'points',
    'point-details',
    'bookings',
    'home',
    'number_check'

]

class LoginRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/media/') or request.path.startswith('/static/'):
            return self.get_response(request)

        current_url_name = resolve(request.path_info).url_name


        if not request.user.is_authenticated:
            if current_url_name not in EXEMPT_URLS:
                return redirect("home")

        return self.get_response(request)


class RoleAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/media/') or request.path.startswith('/static/'):
            return self.get_response(request)


        if not request.user.is_authenticated:
            return self.get_response(request)

        current_url_name = resolve(request.path_info).url_name
        role = request.user.role


        if role == 'barber':
            if current_url_name not in EXEMPT_URLS and current_url_name != 'barber-dashboard':
                return redirect('users:barber-dashboard')

        return self.get_response(request)
