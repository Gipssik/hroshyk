from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, View
from django_twitch_auth.views import TwitchLoginMixin


class HomeView(TemplateView):
    template_name = "home.html"


class LoginView(TwitchLoginMixin, View):
    pass


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse("home"))
